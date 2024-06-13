import openai,os

openai_key = os.getenv("OPENAI_API_KEY")

def ask_ai(message: str):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful CRM assistant."},
            {"role": "user", "content": message},
        ],
    )
    return response.choices[0].message.content
