import requests

class CurrencyConverter:

    API_URL = "https://api.exchangerate.host/latest"

    def __init__(self, base_currency: str = "USD"):
        self.base_currency = base_currency.upper()
        self.rates = self._get_rates()

    def _get_rates(self):
        response = requests.get(f"{self.API_URL}?base={self.base_currency}")
        data = response.json()
        if not data.get("rates"):
            raise ValueError("Не удалось получить курсы валют")
        return data["rates"]

    def convert(self, amount: float, target_currency: str) -> float:
        target_currency = target_currency.upper()
        if target_currency not in self.rates:
            raise ValueError(f"Валюта {target_currency} недоступна")
        return amount * self.rates[target_currency]
