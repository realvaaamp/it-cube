import telebot


bot= telebot.TeleBot('6257317288:AAE7oHUcfKieqClCTTDDGhtg4TWk-YKPeOA')

@bot.message_handler(commands=['start'])
def start(message):
   mess= f'Добро пожаловать,<b>{message.from_user.first_name}</b>,в этом боте представлен ассортимент, когда захочешь что-нибудь купить,напиши нашему менеджеру'
   bot.send_message(message.chat.id, mess, parse_mode='html')
bot.polling(none_stop=True)
    