import requests
from bs4 import BeautifulSoup
import re


def zipcode_checker():

    """ Accept user input for zipcode and weather timeframe
    Check validity of the zipcode by string length and digits only
    Check timeframe entered is from the provided list
    Return True or False and the soup """

    result_dict = {}
    timeframe = ['today', 'hourbyhour', 'tenday', 'weekend']
    base_url = 'https://weather.com/weather'
    zip_code = input("Please enter your 5 digit zipcode: ")

    if len(zip_code) == 5 and zip_code.isdigit() and re.search("^[0-9]{5}", zip_code):
        # if re.search("^[0-9]{5}", zip_code):
            print("Valid ZIP code")
            user_timeframe = input("Please enter the weather timeframe. Options are:"
                                   " today, hourbyhour, tenday or weekend: ")
            if user_timeframe in timeframe:

                url_to_scrape = base_url + '/' + user_timeframe + '/l/' + zip_code
                weather = requests.get(url_to_scrape).text
                return_code = requests.get(url_to_scrape)
                weather_soup = BeautifulSoup(weather, 'lxml')

                if return_code.status_code != 200:
                    print(return_code.status_code)
                    print("Error: The site is down or there are no matches for the zip code provided\n"
                          "Please try another zip code or try again later")
                    return {'status': 'False'}
                else:
                    print(return_code.status_code)
                    result_dict['status'] = 'True'
                    result_dict['timeframe'] = user_timeframe
                    result_dict['soup'] = weather_soup
                    return result_dict

            else:
                print("Timeframe not valid")
                return {'status': 'False'}

    else:
        print("The input was not valid, please enter a 5 digit zipcode: ")
        return {'status': 'False'}





