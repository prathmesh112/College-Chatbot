import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def load_context():
    with open("prompts.txt", "r") as file:
        return file.read()

def ask_bot(user_input):
    context = load_context()
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": context},
            {"role": "user", "content": user_input}
        ],
        max_tokens=300,
        temperature=0.7
    )
    return response.choices[0].message.content.strip()
