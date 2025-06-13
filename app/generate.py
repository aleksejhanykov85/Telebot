from openai import AsyncOpenAI
from handlers import user_dict
from config import AI_TOKEN


client = AsyncOpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=AI_TOKEN,
)

text = f'''Составь меню на неделю
с учетом моих предпочтений: {user_dict['preferences']} и 
моих болезней: {user_dict['diseases']}'''

async def ai_generate(text: str):
  completion = await client.chat.completions.create(
    model="deepseek/deepseek-chat-v3-0324:free",
    messages=[
      {
        "role": "user",
        "content": text
      }
    ]
  )
  print(completion)
  return completion.choices[0].message.content