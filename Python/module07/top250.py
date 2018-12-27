"""
Module 07 - IMBD Parser
"""

import requests
import sys
from bs4 import BeautifulSoup


class ImbdParser():
    """ IMDB Parser Class """
    def __init__(self, arg_url):
        self.url = arg_url
        try:
            self.bs_imdb = BeautifulSoup(requests.get(self.url).text, 'lxml')
        except requests.exceptions.ConnectionError as err:
            print(err)
            sys.exit(1)

    def json_out_file(self, arg_out_file):
        """" Parse HTML page by URL and save it to file in json format"""
        # print(self.bs_imdb.prettify())
        films_data = self.bs_imdb.find('tbody', class_='lister-list')
        for film in films_data.find_all('tr'):
            # print(film.find(class_='titleColumn'))
            print(film.find(class_='titleColumn').a.text)
            print(film.find(class_='titleColumn').a['title'])
            print(film.find(class_='titleColumn').span.text)
            # print('Year:', film.find_all('span','text', class_='titleColumn'))
            # print(film.span.text, end=', ')
            # print(film.td, end=', ')
            # print(film.a.text)


def parse_top_250(arg_out_file):
    imbd_parse_class = ImbdParser('https://imdb.com/chart/top')
    imbd_parse_class.json_out_file(arg_out_file)


if __name__ == "__main__":
    # print("Hello Gold")
    parse_top_250('file_for_saving.json')
