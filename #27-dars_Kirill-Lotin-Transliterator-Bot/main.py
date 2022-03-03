# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 20:41:39 2022

@author: Ulugbek
"""

from transliterate import to_cyrillic, to_latin
import telebot

TOKEN='5209425500:AAHQt6E5XiT_zTqaRy49mdYnlzZfS56TDf8'
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    javob="Assalomu alaykum, Xush kelibsiz"
    javob+="\nAdmin: Ulug\'bek  / @andijondan_salom /"
    javob+="\nWeb sayt: https://ulugbek-links.netlify.app/ \n"
    javob+="\nXatoliklar kuzatilsa adminga murojat qiling. \n"
    javob+="\nBu bot so\'zlarni kirilldan lotinga va lotindan krillga o\'zgartirib beradi."
    javob+="\nMatn kiriting."
    bot.reply_to(message, javob)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg=message.text
    javob=lambda msg:to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    bot.reply_to(message, javob(msg))

bot.infinity_polling()




# matn=input("Matn kiriting.")
# if matn.isascii():
#     print(to_cyrillic(matn))
# else:
#     print(to_latin(matn))
