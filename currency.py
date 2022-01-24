from dataclasses import dataclass
from api import get_currencies


CURRENCIES = get_currencies()


def check_valid_currency(currency: str) -> bool:
    """
    Function that will check currency code is amongst the list of available currencies

    Parameters
    ----------
    currency : str
        Currency code to be checked

    Pseudo-code
    ----------
    IF parsed currency in list of valid currencies derviced from get_currencies function:
        RETURN True
    ELSE:
        RETURN False

    Returns
    -------
    bool
        True if the currency code is valid otherwise False
    """
    # check if parsed currency is in CURRENCIES
    if currency in CURRENCIES:
        return True
    else:
        return False

   


@dataclass
class Currency:
    """
    Class that represents a Currency conversion object. 

    Attributes
    ----------
    from_currency : str
        Code for the origin currency
    to_currency : str
        Code for the destination currency
    amount : float
        The amount (in origin currency) to be converted
    rate : float
        The conversion rate to be applied on the origin amount (origin -> destination)
    inverse_rate : float
        The inverse of the previous rate  (destination -> origin)
    date : str
        Date when the conversion rate was recorded
    """
    
    # class variables
    from_currency: str = None
    to_currency: str = None
    amount: float = 0
    rate: float = 0
    inverse_rate: float = 0
    date: str = None

    def reverse_rate(self):
        """
        Method that will calculate the inverse rate, round it to 5 decimal places and save it in the attribute inverse_rate

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        
        # create inverse rate
        self.inverse_rate = round((1 / self.rate), 5)

    def format_result(self):
        """
        Methods returning the formatted successful message

        Parameters
        ----------
        None

        Returns
        -------
        str
            Formatted successful message
        """
        # => To be filled by student
        result_string = f"Today's {self.date} conversion rate from {self.from_currency} " \
            + f"to {self.to_currency} is {self.rate}. The inverse rate is {self.inverse_rate}"

        return result_string


def extract_api_result(result: dict) -> Currency:
    """
    Function that will extract the relevant fields from API result, instantiate a Currency class accordingly and
    calculate the inverse rate

    Parameters
    ----------
    result : dict
        Results of the API converted as dictionary

    Pseudo-code
    ----------
    SET from_currency TO result of item within base key of dictionary
    SET to_currency TO result of the first position item within the rates key of dictionary
    SET amount TO result of item within amount key of dictionary
    SET rate TO result of item within the to_currency key within the rates key of dictionary
    SET inverse_rate TO None
    SET date TO result of item within the date key of dictionary
    SET instantiated TO result of keyword arguments parsed to Currency class
    Calculate the reverse rate within instantiated class
    RETURN instantiated

    Returns
    -------
    Currency
        Instantiated Currency
    """
    
    
    from_currency = result.get('base')
    to_currency = list(result.get('rates').keys())[0]
    amount  = result.get('amount')
    rate = result.get('rates').get(to_currency)
    inverse_rate = None
    date = result.get('date')
    instantiated = Currency(from_currency = from_currency,
                            to_currency = to_currency,
                            amount = amount,
                            rate = rate, 
                            inverse_rate = inverse_rate,
                            date = date)
    instantiated.reverse_rate()
    return instantiated
