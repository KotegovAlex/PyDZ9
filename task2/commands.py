
import functions as func
from telegram import Update
from telegram.ext import CallbackContext

def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, 
                             text="I'm a bot, what do you want from me?")

def weather(update: Update, context: CallbackContext):
    msg = update.message.text 
    items = msg.split()
    context.bot.send_message(chat_id=update.effective_chat.id, 
                             text=func.weather(items[1]))

def help(update: Update, context: CallbackContext):
    update.message.reply_text('''/start - приветствие перед началом работы
/weather - запрос погоды в определенном городе
/help - справка по боту''')