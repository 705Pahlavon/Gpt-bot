from config import ADMIN_ID
from telegram import Update
from telegram.ext import ContextTypes

async def admin_panel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        return
    await update.message.reply_text("Admin panel: Reklama yuborish uchun matn yuboring.")

async def handle_admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        return
    # Barcha foydalanuvchilarga reklamani yuborish logikasi
    await update.message.reply_text("📢 Reklama yuborildi (bu yerda foydalanuvchi listi bo‘ladi)")
