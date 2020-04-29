import unittest
import random
import requests

zip_code = ['10029', '10028', '75001', '02101', '88901']
timeframe = ['today', 'hourbyhour', 'tenday', 'weekend']
base_url = 'https://weather.com/weather'


class TestScrape(unittest.TestCase):

    """ unit test to perform a quick test of the weather webscraper
    The input is: a random zip code from the zip code list and a random
    timeframe from the timeframe list. The use requests to perform a get on that url
    The output is: Pass if 200 is returned. If not Fail
    """
    def test_(self):
        random_zip = random.choice(zip_code)
        random_timeframe = random.choice(timeframe)
        url_to_scrape = base_url + '/' + random_timeframe + '/l/' + random_zip
        return_code = requests.get(url_to_scrape)
        self.assertEqual(return_code.status_code, 200)


if __name__ == '__main__':
    unitttest.main()



