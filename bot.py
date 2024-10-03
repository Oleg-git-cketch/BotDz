import telebot
import database as db
import buttons as bt



bot = telebot.TeleBot('7595292863:AAGE8wGw0kTQfc1beaJs93DzlJjrbejIa7A')
current_language = 'ru'


@bot.message_handler(commands=['start'])
def start(message):

    user_id = message.from_user.id
    if db.check_user(user_id):
        if current_language == 'ru':
            bot.send_message(user_id, f'Здравствуйте, @{message.from_user.username}!',
                         reply_markup=telebot.types.ReplyKeyboardRemove())
        else:
            bot.send_message(user_id, f'Salom, @{message.from_user.username}!',
                             reply_markup=telebot.types.ReplyKeyboardRemove())
    else:
        bot.send_message(user_id, 'Выберите язык:\n1. Русский\n2. Uzb', reply_markup=bt.ch_language())


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    global current_language
    user_id = call.message.chat.id

    if call.data == 'uzb':
        current_language = 'uzb'
        bot.send_message(user_id, "Til ingliz tiliga o'zgartirildi. Roʻyxatdan oʻtishni boshlaymiz!\nIltimos, ismingizni kiriting!")
        bot.register_next_step_handler(call.message, get_name_uz)
    elif call.data == 'rus':
        current_language = 'ru'
        bot.send_message(user_id, "Язык изменен на русский. Давайте начнем регистрацию!\nВведите ваше имя!")
        bot.register_next_step_handler(call.message, get_name_ru)


def get_name_ru(message):
    user_id = message.from_user.id
    user_name = message.text
    bot.send_message(user_id, 'Отлично! Теперь отправьте свой номер через кнопку!', reply_markup=bt.number_button())
    bot.register_next_step_handler(message, lambda msg: get_number_ru(msg, user_name))


def get_number_ru(message, user_name):
    user_id = message.from_user.id
    if message.contact:
        user_number = message.contact.phone_number
        db.register(user_id, user_name, user_number)
        bot.send_message(user_id, 'Отлично! Теперь отправьте свою локацию через кнопку!')
    else:
        bot.send_message(user_id, '❌ Ошибка! Отправьте свой номер и локацию через кнопки! ❌')
        bot.register_next_step_handler(user_id, get_name_ru)


def handle_location_ru(message):
    user_id = message.from_user.id
    if message.location:
        latitude = message.location.latitude
        longitude = message.location.longitude
        db.location(latitude, longitude)
        bot.send_message(user_id, '✅ Вы успешно зарегистрированы! ✅', reply_markup=telebot.types.ReplyKeyboardRemove())

def get_name_uz(message):
    user_id = message.from_user.id
    user_name = message.text
    bot.send_message(user_id, "Ajoyib! Endi raqamingizni tugmachadan jo\'nating!", reply_markup=bt.uz_number_button())
    bot.register_next_step_handler(message, lambda msg: get_number_uz(msg, user_name))

def get_number_uz(message, user_name):
    user_id = message.from_user.id
    if message.contact:
        user_number = message.contact.phone_number
        db.register(user_id, user_name, user_number)
        bot.send_message(user_id, 'Ajoyib! Endi joylashuvingizni tugmachadan jo\'nating!')
    else:
        bot.send_message(user_id, '❌ Xato! Raqamingiz va joylashuvingizni tugmachalar orqali yuboring! ❌')

def handle_location_uz(message):
    user_id = message.from_user.id
    if message.location:
        latitude = message.location.latitude
        longitude = message.location.longitude
        db.location(latitude, longitude)
        bot.send_message(user_id, '✅ Siz muvaffaqiyatli ro\'yxatdan o\'tganingiz uchun rahmat! ✅', reply_markup=telebot.types.ReplyKeyboardRemove())

@bot.message_handler(content_types=['location'])
def handle_location(message):
    if current_language == 'ru':
        handle_location_ru(message)
    else:
        handle_location_uz(message)

@bot.message_handler(commands=['settings'])
def change_language(message):
    user_id = message.from_user.id
    bot.send_message(user_id, 'Выберите язык:\n1. Русский\n2. Uzb', reply_markup=bt.ch_language())
    bot.register_next_step_handler(message, user_id, callback_query)


bot.polling()