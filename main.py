from telebot.async_telebot import AsyncTeleBot
import asyncio
import telebot as tb
from config import *
from find_func import *
from btn import *

bot = AsyncTeleBot(BOT_API_TOKEN) # В конфиге хранится API-токен
markup = main_btn_update()

@bot.message_handler(commands=['start'])
async def start(message):
        await bot.send_message(message.chat.id, 'Привет, я - бот.', reply_markup=markup)

@bot.message_handler(content_types='text')
async def reply(message):
    print(f"{message.from_user.username}: {message.text}")
    for key, value in rzhunemogu_DICT.items(): 
        if message.text == key: await bot.reply_to(message, tb.formatting.hitalic(rzhunemogu(value)), parse_mode='HTML', reply_markup=fun_markup)
        else: continue
    if message.text == 'Случайные картинки':
        await bot.send_message(message.chat.id, "Выберите вариант картинки", reply_markup=imgs_markup)
    elif message.text == 'Развлечения':
        await bot.send_message(message.chat.id, "Выберите вариант развлечения", reply_markup=fun_markup)
    elif message.text == 'Котик':
        await bot.send_message(message.chat.id, "Обработка запроса... Пожалуйста подождите.")
        await bot.send_photo(message.chat.id, cat_f(), reply_markup=imgs_markup)
    elif message.text == 'Лисичка':
        await bot.send_message(message.chat.id, "Обработка запроса... Пожалуйста подождите.")
        await bot.send_photo(message.chat.id, fox_f(), reply_markup=imgs_markup)
    elif message.text == 'Назад':
        await bot.send_message(message.chat.id, "Выберите функцию", reply_markup=markup)

asyncio.run(bot.infinity_polling())