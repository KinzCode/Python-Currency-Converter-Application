<h1 align="center">Currency Converter </h1>

## Author

**Benjamin McKinnon**

- Student ID: 14391116
- Email: Benjamin.J.Mckinnon@student.uts.edu.au

## Description
A command line application that can calculate the current and reverse rates of two user specified  currencies.

### Available Currencies & Codes
* Australian Dollar = AUD
* Bulgarian Lev = BGN
* Brazilian Real = BRL
* Canadian Dollar = CAD
* Swiss Franc = CHF
* Chinese Yuan = CNY
* Czech Koruna = CZK
* Danish Krone = DKK
* Euro = EUR
* British Pound = GBP
* Hong Kong Dollar = HKD
* Croatian Kuna = HRK
* Hungarian Forint = HUF
* Indonesian Rupiah = IDR
* Israeli New Shekel  = ILS
* Indian Rupee = INR
* Icelandic Króna = ISK
* Japanese Yen= JPY
* South Korean = KRW
* Mexican Peso = MXN
* Malaysian Ringgit = MYR
* Norwegian Krone = NOK
* New Zealand Dollar = NZD
* Philippine peso = PHP
* Poland złoty = PLN
* Romanian Leu = RON
* Russian Ruble = RUB
* Swedish Krona = SEK
* Singapore Dollar = SGD
* Thai Baht = THB
* Turkish lira = TRY
* United States Dollar = USD
* South African Rand  = ZAR

## Available Commands

In the project directory, you can run:

### `python main.py AUD EUR`,

If you are using Pipenv, then you can run:

### `pipenv python main.py AUD EUR`,

## Built With

- Python

## Package Dependencies

- requests

## Structure

    ├── api.py             <- The script containing the methods that format the API url's and call the API.
    ├── currency.py        <- The script containing the method that validates inputted currencies along with the method that extracts the api result using the currency class.
    ├── main.py            <- The script containing the methods that execute the codebase.
    ├── Pipfile            <- Specifies package requirements for development and execution of program.
    ├── Pipfile.lock       <- Specifies and locks the version of the dependencies in Pipfile.
    ├── README.md          <- A markdown file outlining the contents and purpose of the repository along with instructions of how to operate.
    ├── test_api.py        <- The script containing unit tests for the methods that format the API URL, and the method that gets the list of valid currencies.
    └── test_currency.py   <-The script containing unit tests for the method that checks if the user inputted currency is valid, and the methods that extract the API content.

## Functions by Script
### api.py
    ├── call_api   <-  Function that will call the specified API endpoint and return the response.
    ├── format_currencies_url <- Function that will format the URL to the currency endpoint.
    ├── get_currencies <- Function that will extract the currency codes available from the Frankfurter app as a list.
    ├── format_latest_url <- Function that will format the URL to the latest endpoint.
## currency.py
    ├── check_valid_currency <- Function that will check currency code is amongst the list of available currencies
    ├── Class Currency <- Class that represents a Currency conversion object. 
    	├── reverse_rate <- Method that will calculate the inverse rate, round it to 5 decimal places and save it in the attribute inverse_rate.
    	├── format_result <- Methods returning the formatted successful message.
    ├── extract_api_result <- Function that will extract the relevant fields from API result, instantiate a Currency class accordingly and calculate the inverse rate.
## main.py
    ├── def_main <- Function that will check if there are enough input arguments provided. If so it will return the formatted result from the Frankfurter app. If not it will return an error message.
    ├── def_get_rate <- Function that will check if provided currency codes are valid otherwise it will return error message. If both are valid, it will format the API url, make a request to it and format the result.

