from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler,
    ContextTypes, filters
)
from config import BOT_TOKEN, ADMIN_ID
from subscription import check_subscription
from admin import admin_panel, handle_admin
from handlers import chat_with_gpt

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if not await check_subscription(update, context):
        return
    await context.bot.send_message(chat_id=user_id, text="Assalomu alaykum! Menga savol bering:")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("admin", admin_panel))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat_with_gpt))
app.add_handler(MessageHandler(filters.ALL, handle_admin))  # reklamani yuborish
app.run_polling()
