from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes
from database.db import criar_utilizador, definir_idioma
from messages import mensagens

idiomas = [["Português", "English", "Français"]]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    criar_utilizador(user.id)
    await update.message.reply_text(
        "Bem-vindo! Welcome! Bienvenue!
Escolha o seu idioma / Choose your language / Choisissez votre langue:",
        reply_markup=ReplyKeyboardMarkup(idiomas, one_time_keyboard=True)
    )

    context.user_data["aguardando_idioma"] = True

