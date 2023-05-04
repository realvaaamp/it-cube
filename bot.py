import telebot


bot= telebot.TeleBot('6257317288:AAE7oHUcfKieqClCTTDDGhtg4TWk-YKPeOA')

@bot.message_handler(commands=['start'])
def start(message):
    mess= f'Добро пожаловать,<b>{message.from_user.first_name} <u>{message.from_user.last_name}'

    bot.send_message(message.chat.id,mess,"В этом боте преставлены наши вещи,когда захочешь что-то купить,напиши нашему менеджеру^-^")
bot.polling(none_stop=True)
    