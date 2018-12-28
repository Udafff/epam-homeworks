"""
Module 07 - IMBD Parser
"""

import requests
import sys
from bs4 import BeautifulSoup
import json


class ImbdParser():
    """ IMDB Parser Class """
    def __init__(self, arg_url):
        self.url = arg_url
        try:
            self.bs_imdb = BeautifulSoup(requests.get(self.url, headers={"Accept-Language": "En-us"}).text, 'lxml')
        except requests.exceptions.ConnectionError as err:
            print(err)
            sys.exit(1)

    def json_out_file(self, arg_out_file):
        """" Parse HTML page by URL and save it to file in json format"""
        films_data = self.bs_imdb.find('tbody', class_='lister-list')

        lst_top250 = []
        for film in films_data.find_all('tr'):

            film_title = film.find('td', class_='titleColumn').a.text
            position = film.find('td', class_='titleColumn').text.split()[0][:-1]
            year = film.find('td', class_='titleColumn').span.text[1:-1]
            director = film.find(class_='titleColumn').a['title'].split('(dir.),')[0].strip()
            crew = film.find('td', class_='titleColumn').a['title'].split('(dir.),')[1].strip()
            rating = film.find('td', class_='ratingColumn imdbRating').strong.text

            top250 = dict()
            top250[film_title] = {
                "Position": position,
                "Year": year,
                "Director": director,
                "Crew": crew,
                "Rating": rating
            }
            lst_top250.append(top250)

            # ## Another examples for understanding Web Scraping
            # print(repr(film.find(class_='titleColumn').next.replace("\n", "").strip()))
            # print(film.find(class_='titleColumn').next.replace("\n", "").strip()[:-1])
            # print(film.find(class_='titleColumn').next, end='')
            # print('NavigableString:', film('td', class_='titleColumn')[0].next)
            # print('Position[str]:', film.find(class_='titleColumn').contents[0].split()[0])
            # print('Text string of "title" of "a" tag: ', film.find(class_='titleColumn').a['title'])

        try:
            with open(arg_out_file, 'w', encoding='utf8') as fw_handler:

                # print(json.dumps(lst_top250, ensure_ascii=False, indent=1))
                json.dump(lst_top250, fw_handler, ensure_ascii=False)
        except IOError as err:
            print('IOError!!')


def parse_top_250(arg_out_file):
    imbd_parse_class = ImbdParser('https://imdb.com/chart/top')
    imbd_parse_class.json_out_file(arg_out_file)


if __name__ == "__main__":
    # print("Hello Gold")
    parse_top_250("top250.json")
