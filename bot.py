import telebot


bot = telebot.TeleBot('7924443796:AAG9ICEX9BTI_Q8relYTOkDCPTS0uCcGnxA')

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    bot.send_message(user_id, 'Привет')

@bot.message_handler(commands=['help'])
def help(message):
    user_id = message.from_user.id
    bot.send_message(user_id, 'Команды:\n/start (активировать бота)\n/help (помощь по командам бота) ')
bot.polling()