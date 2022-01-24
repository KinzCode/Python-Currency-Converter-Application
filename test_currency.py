import unittest
from currency import check_valid_currency, extract_api_result, Currency


class TestValidCurrency(unittest.TestCase):
    def test_function(self):
        result = check_valid_currency('AUD')
        self.assertEqual(result, True)
    
    def test_false_currency(self):
        result = check_valid_currency('Foo')
        self.assertEqual(result, False)


class TestExtractApi(unittest.TestCase):
    def test_function(self):
        result_dict = {
            'amount': 1.0, 
            'base': 'AUD', 
            'date': '2021-08-06', 
            'rates': {'USD': 0.74373}
            }
        
        result = extract_api_result(result_dict)
        currency = Currency(from_currency='AUD', to_currency='USD', amount=1.0, rate=0.74373, inverse_rate=1.34457, date='2021-08-06')
        self.assertEqual(result, currency)
        
