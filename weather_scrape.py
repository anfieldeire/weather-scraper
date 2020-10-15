from datetime import date
import re

def hourly(result):
    """ scrape hourly weather data and print to screen """

    table = result['soup'].find('table', {'class': 'twc-table'})
    headers = table.find_all('th')[1:]
    weather_dict = {}
    print("Weather forecast: {}".format(result['timeframe']))
    for row in table.find_all('tr'):
        print("\n")
        for time in row.find_all('td', {'headers': 'time'}):
            for div in time:
                div = div.find_all('div', class_=re.compile('^hourly'))
                time = div[0]
                day = div[1]
                print("Time: {},{}".format(time.text, day.text))
        for temp in row.find_all('td', {'class': 'temp'}):
            print("Temperature: {}F".format(temp.text))
        for feels in row.find_all('td', {'class': 'feels'}):
            print("Feels like: {}F".format(feels.text))
        for precip in row.find_all('td', {'class': 'precip'}):
            print("Precipitation: {}".format(precip.text))
        for humidity in row.find_all('td', {'class': 'humidity'}):
            print("Humidity: {}".format(humidity.text))
        for wind in row.find_all('td', {'classname': 'wind'}):
            print("Wind: {}".format(wind.text))
    print("\n")


def today(result):
    """ scrape weather data for today and print to screen """

    today = date.today()
    today_string = today.strftime("%B %d,%Y")
    headers = []
    content = []
    new_dict = {}
    divs = result['soup'].find_all('div', {'class': 'today_nowcard-section today_nowcard-condition'})
    sidecar_div = result['soup'].find('div', class_='today_nowcard-sidecar component panel')
    result['timeframe'] = result['timeframe'].capitalize()
    print("\n{} weather forecast\n".format(result['timeframe']))
    for trs in sidecar_div:
        trs = sidecar_div.find_all('tr')
        for td in trs:
            th = td.find('th')
            headers.append(th.text)
            td_span = td.find('span')
            content.append(td_span)
            new_dict[th.text] = td_span.text
    for div in divs:
        temp_div = div.find('div', {'class': 'today_nowcard-temp'}).text
        print('Weather today: {}'.format(today_string))
        print('Temperature: {}F'.format(temp_div))
    for key, value in new_dict.items():
        print(key,':', value)


def tenday(result):
    """ scrape weather data for the upcoming 10 days and print to screen """

    result['timeframe'] = result['timeframe'].capitalize()
    print("\n{} weather forecast\n".format(result['timeframe']))
    weather_trs = result['soup'].find_all(class_=re.compile("closed"))

    for row in weather_trs:
        trs = row.find_all('td')

    for td in weather_trs:
        days = td.find_all('td', {'headers': 'day'})
        precips = td.find_all('td', {'class': 'precip'})
        temps = td.find_all('td', {'class': 'temp'})
        descriptions = td.find('td', {'classname': 'description'})
        winds = td.find('td', {'class': 'wind'})
        humiditys = td.find('td', {'class': 'humidity'})
        for day in days:
            for element in day:
                element = day.find('span', {'class': 'date-time'})
                date = day.find('span', {'class': 'day-detail clearfix'})
                print("Weather forecast for: {}, {} ".format(element.text, date.text))
        for desc in descriptions:
            print("The outlook is: {}".format(desc.text))
        for temp in temps:
            if '--' in temp.text:
                temp = temp.text.split('--')
                print("Temp: Lows of: {}".format(temp[1]))
            else:
                temp = temp.text.split('°')
                print("Temp: highs of: {}F, lows of: {}F".format(temp[0], temp[1]))
        for precip in precips:
            print("Precipitation: {}".format(precip.text))

        for wind in winds:
            print("Wind: {}".format(wind.text))
        for humidity in humiditys:
            print("Humidity: {}".format(humidity.text))
        print("\n")


def weekend(result):
    """ scrape weather data for the upcoming weekend and print to screen """

    weekend_soup = result['soup'].find_all('div', {'class': 'wx-weather__day'})
    user_timeframe = result['timeframe'].capitalize()
    print("\n{} weather forecast\n".format(user_timeframe))
    for row in weekend_soup:
        row = row.find_all(class_=re.compile('weather-cell$'))
        day_date = row[0].text
        day = day_date[:3]
        date = day_date[3:]
        print("\n{}, {}".format(day, date))
        high_low = row[1].text.replace('F', '')
        high_low = high_low.split('°')
        temp_high = high_low[0]
        temp_low = high_low[1]
        outlook = row[2].text
        precipitation = row[3].text
        wind = row[4].text
        humidity = row[5].text
        print("Temperature, high: {}, low: {}".format(temp_high, temp_low))
        print("The outlook is: {}".format(outlook))
        print("Precipitation: {}".format(precipitation))
        print("Wind: {}".format(wind))
        print("Humidity: {}".format(humidity))








