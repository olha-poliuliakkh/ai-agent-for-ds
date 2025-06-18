#import prompts as pr
import openai

import os
api_key = os.getenv("OPENAI_API_KEY")

client = openai.OpenAI(api_key)

def resp(sys_prompt, us_prompt):
    response = client.chat.completions.create (
    model="gpt-4.1-mini",
    messages = [
        {"role": "system", "content": sys_prompt },
        {"role": "user", "content": us_prompt}
    ])
    return response

