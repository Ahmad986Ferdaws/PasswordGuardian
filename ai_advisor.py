# app/ai_advisor.py

import openai
import os

openai.api_key = os.getenv(\"OPENAI_API_KEY\")

def password_advice(password: str) -> str:
    prompt = (
        f\"Analyze the following password and give a short, helpful security rating "
        f"and improvement tips: '{password}'\"
    )
    response = openai.ChatCompletion.create(
        model=\"gpt-4o\",
        messages=[
            {\"role\": \"system\", \"content\": \"You are a security expert.\"},
            {\"role\": \"user\", \"content\": prompt}
        ]
    )
    return response.choices[0].message.content.strip()

if __name__ == \"__main__\":
    tips = password_advice(\"My$trongPassw0rd!\")
    print(\"Advice:\", tips)
