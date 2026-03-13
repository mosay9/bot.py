import telebot
import random
import string
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = "8525868068:AAFrxqNE5z0SwQrn61Rirt6wqEc2Ci8YbgQ"

bot = telebot.TeleBot(TOKEN)

def generate_username():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(4))

@bot.message_handler(commands=['start'])
def start(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn = KeyboardButton("اقتراح يوزرات شبه رباعي")
    markup.add(btn)
    bot.send_message(message.chat.id, "اختر:", reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == "اقتراح يوزرات شبه رباعي")
def suggest(message):
    username = generate_username()
    bot.send_message(message.chat.id, f"@{username}")

bot.infinity_polling()
