from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from telebot import types


def number_button():
 markup = ReplyKeyboardMarkup(resize_keyboard=True)
 but1= KeyboardButton(text="Отправить номер телефона 📞", request_contact=True)
 but2 = KeyboardButton(text="Отправить локацию ♦️", request_location=True)
 markup.add(but1,but2)
 return markup

def ch_language():
 kb = types.InlineKeyboardMarkup(row_width=2)
 but1 = InlineKeyboardButton(text='Рус', callback_data='rus')
 but2 = InlineKeyboardButton(text='Uzb', callback_data='uzb')
 kb.row(but1, but2)
 return kb

def uz_number_button():
 markup = ReplyKeyboardMarkup(resize_keyboard=True)
 but1= KeyboardButton(text="Qum fon raqami 📞", request_contact=True)
 but2 = KeyboardButton(text="Qum joylashuvi ♦️", request_location=True)
 markup.add(but1,but2)
 return markup

