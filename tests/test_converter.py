import pytest
from unittest.mock import patch
from converter import CurrencyConverter

# Мок ответа API
mock_rates = {
    "EUR": 0.9,
    "RUB": 80.0,
}

@patch("converter.requests.get")
def test_conversion(mock_get):

    mock_get.return_value.json.return_value = {"rates": mock_rates}

    converter = CurrencyConverter("USD")
    result = converter.convert(10, "EUR")
    assert result == 10 * mock_rates["EUR"]

@patch("converter.requests.get")
def test_invalid_currency(mock_get):
    mock_get.return_value.json.return_value = {"rates": mock_rates}

    converter = CurrencyConverter("USD")
    with pytest.raises(ValueError):
        converter.convert(10, "INVALID")