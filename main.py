import sys
from api import call_api, format_latest_url
from currency import check_valid_currency, extract_api_result


def main():
    """
    Function that will check if there are enough input arguments provided.
    If so it will return the formatted result from the Frankfurter app.
    If not it will return an error message

    Parameters
    ----------
    None

    Pseudo-code
    ----------
    If length of program input arguements is equal to 3
       Set formmated_result To the result of parsing sys.argv[1] as from_curreency and sys.argv[2] as to_currency in upper-case to get_rate function
       Return and print the formatted result
    Else:
       Return and print an error message

    Returns
    -------
    str
        Formatted API result or error message
    """
    # check if length of sys.argv is 3
    if len(sys.argv) == 3 :
        # parse from_currency and to _currency to get_rate
        formatted_result = get_rate(from_currency = sys.argv[1].upper(), to_currency = sys.argv[2].upper())
        # return print statement to command line
        return formatted_result
    else:
        # Print error message if len sys.argv != 3
        return print("[ERROR] You haven't provided 2 currency codes")
    
        
    
    
   
def get_rate(from_currency: str, to_currency: str):
    """
    Function that will check if provided currency codes are valid otherwise it will return error message.
    If both are valid, it will format the API url, make a request to it and format the result

    Parameters
    ----------
    from_currency : str
        Currency code to be converted from
    to_currency : str
        Currency code to be converted to

    Pseudo-code
    ----------
    IF first input argument is valid` and second input argument is valid:
        SET url TO the result of format_latest_url function
        SET result TO the result of call_api with input argument as url
        IF result.status_code EQUALS 200:
            SET Currency TO the result of extract_api_result with inpout argument as result in json/dictionary format
            RETURN Formatted result of api call
        Else:
            RETURN print statement of error with api call
    ELSE:
        For currency in list of currencies
            If currency is not valid
                RETURN print statement of currency not being a valid option
   
    Returns
    -------
    str
        Formatted API result or error message
    """
    
    # check valid currency
    if check_valid_currency(from_currency) and check_valid_currency(to_currency):
        # format url with from_currency & to_currency
        url = format_latest_url(from_currency, to_currency)
        # call API with formatted url
        result = call_api(url)
        # Check api call response if 200 continue otherwise return error message
        if result.status_code == 200:
            # Parse API response as JSON
            Currency = extract_api_result(result.json())
            # Return print statement of formatted message to main
            return print((Currency.format_result()))
        else:
            # Print if error with API call
            return print("There is an error with API call")
    else:
        # loop over from and to currency
        for currency in [from_currency, to_currency]:
            # Check if they are false
            if check_valid_currency(currency) is False:
                # return print statement of not being valid
                return print(f"{currency} is not a valid option")

        
 


if __name__ == "__main__":
    main()
