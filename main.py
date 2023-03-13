import telebot
from extensions import ConvertException, CryptoConverter
from config import TOKEN


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = '<Валюта 1> <Валюта 2> <Сколько меняем>. Введите команду /values , чтобы увидеть список всех доступных валют'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Введите нужную валюту'
    for key in keys:
        text = '\n'.join((text, key))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    value = message.text.split()
    if len(value) > 3:
        raise ConvertException('Больше 3 переменных')
    quote, base, ammount = value
    total_base = CryptoConverter.get_price(quote, base, ammount)
    res_total = float (total_base) * float (ammount)
    total_sum = f'Стоимость {ammount} {quote} в {base} равна {res_total}'    
    bot.send_message(message.chat.id, total_sum)


bot.polling()
