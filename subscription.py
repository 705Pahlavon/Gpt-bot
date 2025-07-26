from config import SUB_CHANNELS
from telegram import Update
from telegram.ext import ContextTypes

async def check_subscription(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    for channel in SUB_CHANNELS:
        try:
            member = await context.bot.get_chat_member(chat_id=channel, user_id=user_id)
            if member.status not in ['member', 'creator', 'administrator']:
                raise Exception()
        except:
            await context.bot.send_message(
                chat_id=user_id,
                text=f"⛔ Botdan foydalanish uchun {channel} kanaliga obuna bo‘ling."
            )
            return False
    return True
