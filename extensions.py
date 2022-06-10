import json
import requests

class ConvertionException(Exception):
    pass

class Convertor:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote}&tsyms={base}')
        a_price = json.loads(r.content)[base]
        text = a_price * float(amount)
        return text
