import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

async def chat_with_gpt(update, context):
    user_text = update.message.text
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_text}]
    )
    await update.message.reply_text(response.choices[0].message.content)
