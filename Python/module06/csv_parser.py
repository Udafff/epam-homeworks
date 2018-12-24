import re


class CsvParser:
    """ CSV Parser class """
    def __init__(self, arg_file_name):
        self.file = arg_file_name
        with open(arg_file_name, 'r') as csv_file:
            for line in csv_file:
                print(csv_file.readline())

    def save_as(self):
        pass

    def sell_over(self):
        pass

    def get_country_profit(self):
        pass


if __name__ == "__main__":
    csv_parser = CsvParser('1000 Sales Records.csv')
    pass
