import json
from unittest import TestCase
from unittest.mock import patch
from top250 import parse_top_250
import requests


class TestParseTop250(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mock_data = open('mockImdb.html')

    @classmethod
    def tearDownClass(cls):
        cls.mock_data.close()

    def test_parse_top_250(self):
        link = "https://imdb.com/chart/top"
        # res = requests.get(link, headers={"Accept-Language": "En-us"})
        with patch('top250.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = self.mock_data

            # parse_top_250("top250.json")
            parse_top_250('123')
            print('')
            mocked_get.assert_called_with(link, headers={'Accept-Language': 'En-us'})

            with open("top250.json") as result_json:
                result_data: list = json.load(result_json)
                print(result_data)
                self.assertEqual(list(filter(lambda x: x.get("The Shawshank Redemption") is not None, result_data))[0],
                                 {"The Shawshank Redemption": {"Position": "1", "Year": "1994", "Director": "Frank Darabont",
                                  "Crew": "Tim Robbins, Morgan Freeman", "Rating": "9.2"}})

                self.assertEqual(list(filter(lambda x: x.get("The Godfather") is not None, result_data))[0],
                                 {"The Godfather": {"Position": "2", "Year": "1972", "Director": "Francis Ford Coppola",
                                  "Crew": "Marlon Brando, Al Pacino", "Rating": "9.2"}})

                self.assertEqual(list(filter(lambda x: x.get("Goodfellas") is not None, result_data))[0],
                                 {"Goodfellas":{"Position": "17", "Year": "1990", "Director": "Martin Scorsese",
                                  "Crew": "Robert De Niro, Ray Liotta", "Rating": "8.7"}})
