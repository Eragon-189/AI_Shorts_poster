import os
from openai import OpenAI

api_key = "sk-9e70d61f89ac4dbfbcbb93600ea7644d"
prompt = "Create a short script about drama and relationships. Make the script engaging. Follow the format of this video script: https://www.youtube.com/shorts/mxfvPU7ApX0. The script last about 55 seconds."

def generate_short_script(script_prompt):
    client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")
    response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": script_prompt},
    ],
    stream=False
)
    return response.choices[0].message.content

def main():
    script = generate_short_script(prompt)
    print("Generated Script:")
    print(script)
