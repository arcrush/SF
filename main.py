import telebot
from config import keys, TOKEN
from extensions import Convertor, ConvertionException

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def echo_test(message: telebot.types.Message):
    text = 'Чтобы начать работу введите команду боту в следующем формате:  \
           \n<Имя валюты> <в какую валюту перевести> <количество валюты> \n Увидеть список валют: /values'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def echo_test(message: telebot.types.Message):
    text = 'Доступные валюты: '
    for key in keys.keys():
        text = '\n'.join((text, key,))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise ConvertionException('Слишком много параметров.')

        quote, base, amount = values

        if quote == base:
            raise ConvertionException(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            float(amount)
        except ValueError:
            raise ConvertionException(f'Количество введено не верно: {amount}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {quote}.')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base}.')

    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка пользователя.\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = Convertor.get_price(quote_ticker, base_ticker, amount)
        bot.send_message(message.chat.id, text)

bot.polling()
