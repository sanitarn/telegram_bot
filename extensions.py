import requests
import json


keys = {'Доллар': 'USD', 'Биткоин': 'BTC', 'Евро': 'EUR'}

class ConvertException (Exception):
    pass


class CryptoConverter ():
    @staticmethod
    def get_price(quote: str, base: str, ammount: float)->float:
        if base == quote:
            raise ConvertException('Нельзя вводить одинаковые значения')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertException('Не распознали валюту')
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertException('Не распознали валюту')
        try:
            ammount_ticker = float(ammount)
        except ValueError:
            raise ConvertException('Укажите число, а не текст')

        total_base = requests.get(
            f'https://min-api.cryptocompare.com/data/price?fsym={keys[quote]}&tsyms={keys[base]}')
        result = json.loads(total_base.content)[keys[base]]
        # result = float(text) * ammount
        return result
