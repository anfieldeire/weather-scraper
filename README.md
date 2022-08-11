# weather-scraper
The project scrapes weather information from weather.com based on 2 user provided inputs
  - zipcode (5 digit)
  - timeframe: hourly, today, tenday, weekend

## Prerequisites
Python 3.6 (tested on version 3.6 only)

 ## Install the following modules:
 - install bs4
 - install requests
 - install re
 - install datetime
 - install random

## Installation
 - Download the 3 python files and the requirements.txt file
 - Copy the python files (and the requirements.txt) into the virtual environment scripts folder /Scripts
 - Activate the virtual environment
 - Install the pre-requisite packages by running from command prompt: pip install requirements.txt
## Running the program
- From command line run weather.py
  - Enter the zip code for where you want the weather scraped
  - Enter the timeframe from the list provided
  - The output with the weather forecase will print to screen
## Testing
- Just run the test_scrape file. If it returns 200, test passed. Otherwise it will fail
  


