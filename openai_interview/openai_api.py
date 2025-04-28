import openai
import os

with open('OpenAIAPIKey.txt') as f:
    key = f.read().split('=')[1].strip()

openai.api_key = key

def generate_question(topic, previous_answer=None):
    if previous_answer:
        prompt = f"Given the previous answer: {previous_answer}, ask a deeper interview question on {topic}."
    else:
        prompt = f"Ask a basic interview question about {topic}."
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']
