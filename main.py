import telebot
import configure
import types

bot = telebot.TeleBot('5360883455:AAHk4kyImiqL5VS7Vd4Xwz9AmCVubGwfut4')

@bot.message_handler(commands=['get_info','info'])
def get_user_info(message):
    markup_inline = types.InlineKeyboardMarkup()
    item_yes = types.InlineKeyboardButton(text='Да', callback_data = 'yes')
    item_no = types.InlineKeyboardButton(text='Нет', callback_data = 'no')

    markup_inline.add(item_yes, item_no)
    bot.send_message(message.chat.id, 'Информация о пользователе',
        reply_markup=markup_inline
    )

@bot.callback_query_handler(func = lambda call: True)
def answer(call):
    if call.data == 'yes':
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
        

@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('Pic/welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    bot.send_message(message.chat.id, 
    "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b> тестовый бот для помощи в поиске информации.".
    format(message.from_user, bot.get_me()),parse_mode='html'
    )

@bot.message_handler(content_types=['text'])
def text(message):
    bot.send_message(message.chat.id, message.text)

bot.polling(none_stop = True, interval = 0) 