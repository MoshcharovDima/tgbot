import telebot
from config import *
from api import APIException, Convertor
import traceback
botik = telebot.TeleBot(TOKEN)


@botik.message_handler(commands=['start'])
def start(message: telebot.types.Message):
    text = "Приветсвую! Я бот-конвертер, я умею переводить выбраные вами валюты\n \
Вводите сообщения в таком виде,чтобы получить желаемый результат:\n\
<Имя валюты>\n\
<Новая валюта>\n\
<Интересующее количество>\n\
С помощью команды /values можно ознакомиться со списком доступных валют\n\
Для получения инструкции по искользованию введите команду /help"
    botik.send_message(message.chat.id, text)


@botik.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = "Доступные валюты:"
    for i in exchanges.keys():
        text = '\n'.join((text, i))
    botik.reply_to(message, text)


@botik.message_handler(commands=['help'])
def start(message: telebot.types.Message):
    text = "Вводите сообщения в таком виде,чтобы получить желаемый результат:\n\
<Имя валюты>\n\
<Новая валюта>\n\
<Интересующее количество>\n\
С помощью команды /values можно ознакомиться со списком доступных валют"
    botik.send_message(message.chat.id, text)


@botik.message_handler(content_types=['text'])
def converter(message: telebot.types.Message):
    values = message.text.split()
    try:
        if len(values) != 3:
            raise APIException('Неверное количество параметров!')

        answer = Convertor.get_price(*values)
    except APIException as e:
        botik.reply_to(message, f"Ошибка в команде:\n{e}")
    except Exception as e:
        traceback.print_tb(e.__traceback__)
        botik.reply_to(message, f"Неизвестная ошибка:\n{e}")
    else:
        botik.reply_to(message, answer)


botik.polling()






