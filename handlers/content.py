from telegram import Update
from telegram.ext import ContextTypes
from database.db import salvar_comprovativo, tem_acesso
from messages import mensagens

async def receber_comprovativo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    doc = update.message.document
    if doc:
        file = await doc.get_file()
        file_path = f"comprovativos/{user_id}.pdf"
        await file.download_to_drive(file_path)
        salvar_comprovativo(user_id)
        await update.message.reply_text("Comprovativo recebido. Aguarde aprovação.")

async def conteudo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if tem_acesso(user_id):
        lang = "pt"  # Simples: sempre português por enquanto
        await update.message.reply_text(mensagens[lang]["premium"])
    else:
        await update.message.reply_text("Assinatura não ativa. Envie comprovativo para acesso.")
