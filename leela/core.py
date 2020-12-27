from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os
from .config import PORT

TOKEN = ''


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
                                    text="Oi, Eu sou Leela! Já tem seu chip de profissão?")

def main():
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    updater.start_webhook(listen="0.0.0.0",
                           port=PORT,
                           url_path=TOKEN)
    updater.bot.setWebhook('https://leela-bot.herokuapp.com/' + TOKEN)

    #updater.start_polling()

    #updater.idle()