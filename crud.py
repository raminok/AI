from sqlalchemy.orm import Session
import models, schemas

def get_customers(db: Session):
    return db.query(models.Customer).all()

def create_customer(db: Session, customer: schemas.CustomerCreate):
    db_customer = models.Customer(**customer.dict())
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer
