import telebot
from telebot import types
import random

bot = telebot.TeleBot("893696573:AAG2Sw38lNz3JFLYfXGK7gr4yJzEaZqkh24")

PHRASE = ['aaa', 'bbb', 'ddd', 'fff']
QUOTES = ['Чтобы хорошо жить, нужно много работать. А для того, чтобы стать богатым, нужно придумать что-то другое.',
          'Выбирая цель, цельтесь выше, не боясь попасть в звёзды.',
          'Не бойся быть ни как все и все захотят быть как ты!',
          'Выгоднее всего продавать людям их мечты…',
          ' Бизнес - это сочетание войны и спорта.',
          'Сделайте так, чтобы все гадали о вашем следующем шаге. Не будьте слишком предсказуемым.',
          'В мире бизнеса зеркало заднего вида всегда чище переднего стекла',
          'Никогда не инвестируй в бизнес, в котором ничего не понимаешь.',
          'Первая и главная предпосылка успеха в бизнесе - это терпение.',
          'Чтобы хорошо жить, нужно много работать. А для того, чтобы стать богатым, нужно придумать что-то другое.']
secure_random = random.SystemRandom()

lon = 43.236841
lan = 76.927286

markup_menu = types.ReplyKeyboardMarkup(resize_keyboard=False, row_width=1)
btn1 = types.KeyboardButton('Записаться на бесплатный бизнес практикум в Алматы')
btn2 = types.KeyboardButton('Записаться на бесплатный бизнес-практикум онлайн с любого города')
btn3 = types.KeyboardButton('Записаться на закрытую встречу для действующих предпринимателей')
btn4 = types.KeyboardButton('Записаться на 2-х дневный курс АТОМ')
btn5 = types.KeyboardButton('Записаться на 7-ми недельный курс МОНСТА')
btnTime = types.KeyboardButton('Узнать ближайшие мероприятия:')
btnInfo = types.KeyboardButton('У меня есть вопрос:')
btnLoc = types.KeyboardButton('Адрес')
btnQ = types.KeyboardButton('Цитата на день')
markup_menu.add(btn1, btn2, btn3, btn4, btn5, btnTime, btnInfo, btnQ, btnLoc)

keyboard = types.InlineKeyboardMarkup()
key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
keyboard.add(key_yes)
key_no = types.InlineKeyboardButton(text='Нет', url="https://monsta.kz/")
keyboard.add(key_no)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, 'Привет! чем я могу тебе помочь?', reply_markup=markup_menu)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == 'Записаться на бесплатный бизнес практикум в Алматы':
        bot.reply_to(message, 'test1')
    elif message.text == 'Записаться на бесплатный бизнес-практикум онлайн с любого города':
        bot.reply_to(message, 'https://monsta.kz/')
    elif message.text == 'Записаться на закрытую встречу для действующих предпринимателей':
        bot.reply_to(message, 'test3')
    elif message.text == 'Записаться на 2-х дневный курс АТОМ':
        bot.reply_to(message, 'test4')
    elif message.text == 'Записаться на 7-ми недельный курс МОНСТА':
        bot.reply_to(message, 'test5')
    elif message.text == 'Узнать ближайшие мероприятия:':
        bot.reply_to(message, 'test6')
    elif message.text == 'У меня есть вопрос:':
        text = "test7"
        bot.send_message(message.chat.id, text=text, reply_markup=keyboard)
    elif message.text == 'Цитата на день':
        bot.reply_to(message, secure_random.choice(QUOTES))
    elif message.text == 'Адрес':
        bot.send_message(message.chat.id, 'Adress')
        bot.send_venue(message.chat.id, lon, lan, 'Гранд Айсер отель', 'Pozharsky 1, Алматы')
    else:
        bot.reply_to(message, secure_random.choice(PHRASE), reply_markup=markup_menu)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes":
        bot.send_message(call.message.chat.id, "Horosho", reply_markup=markup_menu)


bot.polling()
