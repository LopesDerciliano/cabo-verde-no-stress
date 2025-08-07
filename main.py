from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from handlers.start import start
from handlers.admin import aprovar, rejeitar, ver_utilizadores, notificar
from handlers.content import receber_comprovativo, conteudo

import os
from dotenv import load_dotenv

load_dotenv()
app = ApplicationBuilder().token(os.getenv("BOTTOKEN")).build()

# Handlers
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("aprovar", aprovar))
app.add_handler(CommandHandler("rejeitar", rejeitar))
app.add_handler(CommandHandler("ver_utilizadores", ver_utilizadores))
app.add_handler(CommandHandler("notificar", notificar))
app.add_handler(MessageHandler(filters.Document.ALL, receber_comprovativo))
app.add_handler(CommandHandler("conteudo", conteudo))

app.run_polling()
