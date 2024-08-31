# We thought of giving you a gift this new year by sharing the web scraping script
# Understanding the script before using is always appreciated
# We left few blanks in the script for your exploration
# Make sure to replace FILL_IN_THE_BLANK in the code to make it work

import requests
import numpy as np
from bs4 import BeautifulSoup

def scrapper(imdbId):
    id = str(int(imdbId))
    n_zeroes = 7 - len(id)
    new_id = "0" * n_zeroes + id
    URL = f"https://www.imdb.com/title/tt{new_id}/"
    request_header = {
        'Content-Type': 'text/html; charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0',
        'Accept-Encoding': 'gzip, deflate, br'
    }
    response = requests.get(URL, headers=request_header)
    soup = BeautifulSoup(response.text, 'lxml')

    # Replace with actual class name for IMDb rating
    imdb_rating_element = soup.find('span', attrs={'class': '"sc-40b53d-1 kJANdR"'})  # Adjust as needed
    imdb_rating = imdb_rating_element.text if imdb_rating_element else 'Rating not found'
    
    return imdb_rating

# Test the function with a known IMDb ID
print(scrapper(tt0113228))  # Replace with actual IMDb ID
