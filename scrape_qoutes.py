from http.client import responses

import requests
from bs4 import BeautifulSoup


#Step 1: Send HTTP request
url = "https://quotes.toscrape.com"
response = requests.get(url)

#Step 2: Parse HTML with BeuatifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

#Step 3 : Extract quaotes and authors
quotes = soup.find_all('div', class_ = 'quote')

for quote in quotes:
    text = quote.find('span', class_ = 'text').text
    author = quote.find('small', class_ = 'author').text
    print(f"{text} - {author}")