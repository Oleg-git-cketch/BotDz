from telebot.types import ReplyKeyboardMarkup, KeyboardButton

def number_button():
 markup = ReplyKeyboardMarkup(resize_keyboard=True)
 but1= KeyboardButton(text="Отправить номер телефона", request_contact=True)
 but2 = KeyboardButton(text="Отправить локацию", request_location=True)
 markup.add(but1,but2)
 return markup