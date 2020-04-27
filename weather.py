from zipcode_checker import zipcode_checker
import weather_scrape


if __name__ == "__main__":
    result = zipcode_checker()

    if result['status'] == 'True':

        if result['timeframe'] == 'hourbyhour':
            weather_scrape.hourly(result)
        elif result['timeframe'] == 'today':
            weather_scrape.today(result)
        elif result['timeframe'] == 'tenday':
            weather_scrape.tenday(result)
        elif result['timeframe'] == 'weekend':
            weather_scrape.weekend(result)















