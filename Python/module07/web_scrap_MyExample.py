""""
Module 07 - My Web Scraping learning example
"""

import requests
from bs4 import BeautifulSoup


class WebScrap:
    """ This example parses Quotes from http://quotes.toscrape.com/ """
    def __init__(self, arg_url):
        self.url = arg_url
        self.bs_html = BeautifulSoup(requests.get(self.url).text, 'lxml')

    def get_pretty_soup(self):
        print(self.bs_html.prettify())

    def get_by_tag(self):
        # Get by using tag-to-tag method (first entry of tag)
        print('Get by tag-to-tag:\t', self.bs_html.div.div.a.text)
        # Get a child by index from list of elements
        print('Get by index:\t\t', self.bs_html.head.contents[3].text)

    def find_div(self):
        print('Get by find(tag):\t', self.bs_html.find('div').div.a.text)

    def get_by_class(self):
        # header = self.bs_html.find_all('div', class_='col-md-8')
        print('Get by find(class):\t', self.bs_html.find(class_="col-md-8").a.text)

    def get_quotes(self):
        """ Get all quotes Method from http://quotes.toscrape.com/"""
        for quote in self.bs_html.find_all('span', class_='text'):
            print('\t', quote.text)

    def get_quotes_list(self):
        lst_quotes = [quote.text for quote in self.bs_html.find_all('span', class_='text')]
        return lst_quotes


if __name__ == "__main__":
    # print("Hello Gold")
    cls_scrap = WebScrap('http://quotes.toscrape.com/')
    # cls_scrap.get_pretty_soup()
    cls_scrap.get_by_tag()
    cls_scrap.find_div()
    cls_scrap.get_by_class()
    cls_scrap.get_quotes()

    print('Print from list:', cls_scrap.get_quotes_list()[0])
