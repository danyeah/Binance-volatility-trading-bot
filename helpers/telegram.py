import os
import telebot

bot = telebot.TeleBot("__YOUR_API_KEY")
CHAT_ID = "__YOUR_CHAT_ID__"
@bot.message_handler(commands=['start', 'help'])

def send_telegram(msg):
    bot.send_message(CHAT_ID, {msg})

