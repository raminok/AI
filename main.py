from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import models, schemas, crud, ai_service
from database import engine, SessionLocal

# ساخت جداول در دیتابیس
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI + CRM Demo")

# Dependency برای سشن دیتابیس
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "Welcome to AI-CRM Backend"}

@app.get("/customers/", response_model=list[schemas.Customer])
def list_customers(db: Session = Depends(get_db)):
    return crud.get_customers(db)

@app.post("/customers/", response_model=schemas.Customer)
def add_customer(customer: schemas.CustomerCreate, db: Session = Depends(get_db)):
    return crud.create_customer(db, customer)

@app.post("/chat/")
def chat_with_ai(chat: schemas.ChatRequest):
    reply = ai_service.ask_ai(chat.message)
    return {"response": reply}
