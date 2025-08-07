from telegram import Update
from telegram.ext import ContextTypes
from database.db import aprovar_user, rejeitar_user, listar_utilizadores, listar_ids_ativos
import os

ADMIN_ID = int(os.getenv("ADMIN_ID"))

def admin_only(func):
    async def wrapper(update: Update, context: ContextTypes.DEFAULT_TYPE):
        if update.effective_user.id != ADMIN_ID:
            await update.message.reply_text("Acesso negado.")
            return
        await func(update, context)
    return wrapper

@admin_only
async def aprovar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        user_id = int(context.args[0])
        aprovar_user(user_id)
        await update.message.reply_text(f"Utilizador {user_id} aprovado.")
    else:
        await update.message.reply_text("Forneça o ID do utilizador.")

@admin_only
async def rejeitar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        user_id = int(context.args[0])
        rejeitar_user(user_id)
        await update.message.reply_text(f"Utilizador {user_id} rejeitado.")
    else:
        await update.message.reply_text("Forneça o ID do utilizador.")

@admin_only
async def ver_utilizadores(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lista = listar_utilizadores()
    mensagem = "\n".join([f"{u[0]} - {u[1]}" for u in lista])
    await update.message.reply_text(mensagem or "Nenhum utilizador.")

@admin_only
async def notificar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        texto = " ".join(context.args)
        for uid in listar_ids_ativos():
            await context.bot.send_message(uid, texto)
        await update.message.reply_text("Mensagem enviada.")
    else:
        await update.message.reply_text("Envie a mensagem após o comando.")
