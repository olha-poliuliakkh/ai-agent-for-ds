import openai
import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def resp(sys_prompt, us_prompt):
    response = client.chat.completions.create (
    model="gpt-4.1-mini",
    messages = [
        {"role": "system", "content": sys_prompt},
        {"role": "user", "content": us_prompt}
    ])
    return response

