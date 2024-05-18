import requests as r
import telebot as tb
from telebot.async_telebot import AsyncTeleBot
from btn import *
from random import randint
from config import BOT_API_TOKEN

bot = AsyncTeleBot(BOT_API_TOKEN)

def rzhunemogu(rate):
    url = f'http://rzhunemogu.ru/RandJSON.aspx?CType={rate}'
    reply_text = r.get(url).text.replace('{"content":"', '').replace('"}', '')
    return reply_text

def main_btn_update():
    markup = tb.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    markup.add(imgs, fun)
    return markup

def cat_f():
    return r.get("https://theoldreader.com/kittens/600/400/").content

def fox_f():
    return r.get(f"https://randomfox.ca/images/{randint(1, 123)}.jpg").content