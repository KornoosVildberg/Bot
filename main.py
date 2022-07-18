from distutils.log import info
from email import message
import telebot
from telebot import types

bot = telebot.TeleBot('5360883455:AAHk4kyImiqL5VS7Vd4Xwz9AmCVubGwfut4')


@bot.message_handler(commands=["start"])
def welcome(message):
    sti = open('Pic/testing.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    bot.send_message(message.chat.id, 
    "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b> тестовый бот для помощи в поиске информации.".
    format(message.from_user, bot.get_me()),parse_mode='html'
    )

@bot.message_handler(commands=['menu'])
def menu(message):
    markup_inline = types.InlineKeyboardMarkup()
    item_weather = types.InlineKeyboardButton(text = 'Погода', callback_data = 'weather')
    item_about = types.InlineKeyboardButton(text = 'О пользователе', callback_data = 'about')
    item_guide = types.InlineKeyboardButton(text = 'Справочник', callback_data = 'guide')

    markup_inline.add(item_about, item_guide, item_weather)
    bot.send_message(message.chat.id, 
    'Меню',
    reply_markup = markup_inline
    )

@bot.callback_query_handler(func = lambda call: True)
def answer(call):
    if call.data == 'weather':
        bot.send_message(call.message.chat.id,
        'test')

    elif call.data == 'about':
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
        item_id = types.KeyboardButton('Мой ID')
        item_username = types.KeyboardButton('Мой ник')
        markup_reply.add(item_id, item_username)
        bot.send_message(call.message.chat.id, 'Выберите необходимый пункт.',
        reply_markup= markup_reply
        )

    elif call.data == 'guide':
        bot.send_message(call.message.chat.id,
        'test')


@bot.message_handler(content_types = ['text'])
def get_about(message):
    if message.text == 'Мой ID':
        bot.send_message(message.chat.id,
        f'Ваш ID: {message.from_user.id}')
    elif message.text == 'Мой ник':
        bot.send_message(message.chat.id,
        f'Ваш ник: {message.from_user.first_name} {message.from_user.last_name}')

bot.polling(none_stop = True, interval = 0) 