# Currency Converter

Простой конвертер валют на Python с использованием API https://exchangerate.host

## Установка
pip install requests

## Пример использования
from converter import CurrencyConverter

converter = CurrencyConverter("USD")
print(converter.convert(10, "EUR"))
