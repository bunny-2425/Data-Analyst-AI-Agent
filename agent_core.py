import os
from dotenv import load_dotenv
from together import Together

load_dotenv()
client = Together()

MODEL = "meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8"

def ask_agent(file_context, user_question):
    system_prompt = (
        "You are a helpful AI Data Analyst Agent. "
        "Use the provided data context to answer the user's question. "
        "If the context is irrelevant, respond politely."
    )

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"Context:\n{file_context}\n\nQuestion: {user_question}"}
    ]

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=0.7,
        max_tokens=512
    )

    return response.choices[0].message.content.strip()