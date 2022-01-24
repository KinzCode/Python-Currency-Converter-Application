import requests


_HOST_ = 'https://api.frankfurter.app'
_CURRENCIES_ = '/currencies'
_LATEST_ = '/latest'


def call_api(url: str) -> requests.models.Response:
    """
    Function that will call the specified API endpoint and return the response

    Parameters
    ----------
    url : str
        URL of the API endpoint to be called

    Pseudo-code
    ----------
    
    SET response TO result of requests.get with parsed url 
    RETURN response object

    Returns
    -------
    requests.models.Response
        Response from API request
    """
    
    # request response object with parsed url
    response = requests.get(url)
    return response

def format_currencies_url() -> str:
    """
    Function that will format the URL to the currency endpoint

    Parameters
    ----------
    None

    Pseudo-code
    ----------
    SET currencies_url TO result of _HOST_ + _CURRENCIES_ concatenation 
    RETURN a formatted url

    Returns
    -------
    str
        Formatted URL to the currency endpoint
    """
    
    # concat _HOST_ and _CURRENCIES_ string to make currencies_url
    currencies_url = _HOST_ + _CURRENCIES_
    return currencies_url


def get_currencies():
    """
    Function that will extract the currency codes available from the Frankfurter app as a list

    Parameters
    ----------
    None

    Pseudo-code
    ----------
    SET currencies_url TO result of format_currencies_url function
    SET result TO the returned result of call_api function with currncies_url as parsed arguement
    SET currency_list TO result of getting all currencies which are dictionary keys in the json result object
    RETURN a list of all currencies available from the API

    Returns
    -------
    list
        Currency codes available from the Frankfurter app
    """
    # call format_currencies_url function
    currencies_url = format_currencies_url()
    # parse currencies_url into call_api function
    result = call_api(currencies_url)
    # list comprehension on result to get currency codes
    currency_list = [i for i in result.json().keys()]
    return currency_list
        


def format_latest_url(from_currency: str, to_currency: str) -> str:
    """
    Function that will format the URL to the latest endpoint

    Parameters
    ----------
    from_currency : str
        Currency code to be converted from
    to_currency : str
        Currency code to be converted to

    Pseudo-code
    ----------
    SET path TO result of f string embedding the from and to currency into api path format
    SET url TO result of concatentation of  _HOST_ + _LATEST_ + path
    RETURN formatted url 
    
    Returns
    -------
    str
        Formatted URL to the latest endpoint
    """
    # f string with from_currency and to_currency to create path string
    path = f"?from={from_currency}&to={to_currency}"
    # concat path to _HOST_ and _LATEST to create API endpoint
    url = _HOST_ + _LATEST_ + path
    return url

