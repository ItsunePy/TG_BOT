import telebot as tb
import requests
from config import *
from find_func import *
from btn import *

bot = tb.TeleBot(BOT_API_TOKEN) # В конфиге хранится API-токен
markup = main_btn_update()

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, я - бот.', reply_markup=markup)

@bot.message_handler(content_types='text')
def reply(message):
    for key, value in rzhunemogu_DICT.items(): 
        if message.text == key: bot.reply_to(message, tb.formatting.hitalic(rzhunemogu(value)), parse_mode='HTML', reply_markup=fun_markup)
        else: continue
    if message.text == 'Случайные картинки':
        bot.send_message(message.chat.id, "Выберите вариант картинки", reply_markup=imgs_markup)
    elif message.text == 'Развлечения':
        bot.send_message(message.chat.id, "Выберите вариант развлечения", reply_markup=fun_markup)
    elif message.text == 'Котик':
        bot.send_message(message.chat.id, "Обработка запроса... Пожалуйста подождите.")
        bot.send_photo(message.chat.id, cat_f(), reply_markup=imgs_markup)
    elif message.text == 'Лисичка':
        bot.send_message(message.chat.id, "Обработка запроса... Пожалуйста подождите.")
        bot.send_photo(message.chat.id, fox_f(), reply_markup=imgs_markup)
    elif message.text == 'Назад':
        bot.send_message(message.chat.id, "Выберите функцию", reply_markup=markup)

bot.infinity_polling()