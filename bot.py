import telebot
import database as db
import buttons as bt


bot = telebot.TeleBot('7595292863:AAGE8wGw0kTQfc1beaJs93DzlJjrbejIa7A')

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    if db.check_user(user_id):
        bot.send_message(user_id, 'Привет!')
    else:
        bot.send_message(user_id, 'Привет! Давайте начнем регистрацию!\nВведите ваше имя!')
        bot.register_next_step_handler(message, get_name)

def get_name(message):
    user_id = message.from_user.id
    user_name = message.text
    bot.send_message(user_id, 'Отлично! теперь отправьте свой номер через кнопку!', reply_markup=bt.number_button())
    bot.register_next_step_handler(message, get_number, user_name)

def get_number(message, user_name):
    user_id = message.from_user.id
    if message.contact:
        user_number = message.contact.phone_number
        bot.send_message(user_id, 'Отлично! теперь отправьте свою локацию через кнопку!')
        db.register(user_id, user_name, user_number)
    else:
        bot.send_message(user_id, 'Отправьте свой номер и локацию через кнопки!')

@bot.message_handler(content_types=['location'])
def handle_location(message):
    user_id = message.from_user.id
    if message.location:
     latitude = message.location.latitude
     longitude = message.location.longitude
     db.location(latitude, longitude)
     bot.send_message(user_id, 'Вы успешно зарегестрированы!')
    else:
        bot.send_message(user_id, 'Отправьте свой номер и локацию через кнопки!')

bot.polling()