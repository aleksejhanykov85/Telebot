from openai import AsyncOpenAI
from dotenv import load_dotenv

import os

load_dotenv()
AI_TOKEN = int(os.getenv('AI_TOKEN',0))

client = AsyncOpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=AI_TOKEN,
)



async def ai_generate(text: str):
  completion = await client.chat.completions.create(
    model="deepseek/deepseek-r1-0528:free",
    messages=[
      {
        "role": "user",
        "content": text
      }
    ]
  )
  print(completion)
  return completion.choices[0].message.content

