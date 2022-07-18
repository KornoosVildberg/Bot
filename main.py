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

    markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item_weather = types.InlineKeyboardButton(text = 'Погода', callback_data = 'weather')
    item_about = types.InlineKeyboardButton(text = 'О пользователе', callback_data = 'about')
    item_guide = types.InlineKeyboardButton(text = 'Справочник', callback_data = 'guide')

    markup_reply.add(item_guide, item_weather, item_about)
    bot.send_message(message.chat.id, 'Выберите необходимый пункт:',
    reply_markup = markup_reply 
    )

@bot.message_handler(content_types = ['text'])
def get_choose(message):
    if message.text == 'Погода':
        bot.send_message(message.chat.id,
        f'функция в разработке')
    elif message.text == 'О пользователе':
        bot.register_next_step_handler(message, get_about)
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
        item_id = types.KeyboardButton('Мой ID')
        item_username = types.KeyboardButton('Мой ник')
        markup_reply.add(item_id, item_username)
        bot.send_message(message.chat.id, 'Что именно Вас интересует?',
        reply_markup = markup_reply
        )
    elif message.text == 'Справочник':
        bot.send_message(message.chat.id,
        f'функция в разработке')

@bot.message_handler(content_types = ['text'])
def get_about(message):
    if message.text == 'Мой ID':
        bot.send_message(message.chat.id,
        f'Ваш ID: {message.from_user.id}')
    elif message.text == 'Мой ник':
        bot.send_message(message.chat.id,
        f'Ваш ник: {message.from_user.first_name} {message.from_user.last_name}')

bot.polling(none_stop = True, interval = 0) 