import telebot
from telebot import types

bot = telebot.TeleBot('6871427421:AAF2WAK3Kh7O4gVcue_tmjAMkGlJUuWgF68')

@bot.message_handler(commands=['start'])
def main(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Продукция', callback_data='products')
    btn2 = types.InlineKeyboardButton('Где найти?', callback_data='adress')
    markup.add (btn1, btn2)
    btn3 = types.InlineKeyboardButton('Дистрибьюторам', callback_data='distr')
    btn4 = types.InlineKeyboardButton('Контакты', callback_data='contact')
    markup.add(btn3, btn4)
    btn5 = types.InlineKeyboardButton('Задать вопрос', callback_data='question')
    markup.add(btn5)
    bot.send_message(message.from_user.id, f'Привет, {message.from_user.first_name}! Мне не терпится начать работу с Вами. Что Вас интересует?', reply_markup=markup)


bot.polling(none_stop=True)
