import telebot
import config
import random

from telebot import types

bot= telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    sti=open('static/welcome.webp','rb')
    bot.send_message(message.chat.id,"Добро пожаловать, {0.first_name}!/nВ этом боте преставлены наши вещиБкогда захочешь что-то купить,напиши нашему менеджеру:)")
@bot.message_handler(content_types=["text"])
def lalala(message):
    bot.send_message(message.chat.id,message.text)

    #run
    bot.polling(none_stop=True)