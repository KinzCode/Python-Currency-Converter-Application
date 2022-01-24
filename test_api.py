import unittest
from api import call_api, format_currencies_url, get_currencies, format_latest_url, _HOST_, _LATEST_, _CURRENCIES_


class TestFormatUrl(unittest.TestCase):
    def test_function_currencies(self):
        format_currencies = format_currencies_url()
        self.assertEqual(type(format_currencies), str)
        self.assertEqual(format_currencies, 'https://api.frankfurter.app/currencies')
   
    def test_function_url(self):
        format_latest = format_latest_url('USD', 'AUD')
        self.assertEqual(type(format_latest), str)
        self.assertEqual(format_latest, 'https://api.frankfurter.app/latest?from=USD&to=AUD')
    

class TestAPI(unittest.TestCase):
    def test_function(self):
        result_currencies = get_currencies()
        self.assertEqual(type(result_currencies), list)
                         
