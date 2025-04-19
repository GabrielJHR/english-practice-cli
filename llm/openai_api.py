import os
import openai
import json

def initialize_openai(api_key):
    openai.api_key = api_key

def send_message_to_llm(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message['content']

def load_api_key_from_env():
    return os.getenv("OPENAI_API_KEY")