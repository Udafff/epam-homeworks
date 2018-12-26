import csv

from bs4 import BeautifulSoup

import requests


resp = requests.get("http://quotes.toscrape.com")
soup = BeautifulSoup(resp.text, 'lxml')
for quote in soup.find_all(class_='quote'):
    quote_text = quote.span.text
    quote_author = quote.small.text
    tags = [tag.text for tag in quote.find_all(class_="tag")]
    with open("quotes.csv", 'a') as w_csv:
        csv_writer = csv.writer(w_csv)
        csv_writer.writerow([quote_text, quote_author, tags])
