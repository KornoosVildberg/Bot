import telebot
import configure

bot = telebot.TeleBot('5360883455:AAHk4kyImiqL5VS7Vd4Xwz9AmCVubGwfut4')

@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('Pic/welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b> тестовый бот для помощи поиска информации.".format(message.from_user, bot.get_me()),parse_mode='html')

@bot.message_handler(content_types=['text'])
def text(message):
    bot.send_message(message.chat.id, message.text)

bot.polling(none_stop = True, interval = 0) 