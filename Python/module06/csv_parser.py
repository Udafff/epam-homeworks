"""
Module 06 - Csv Parser
"""

import csv


class CsvParser:
    """ CSV Parser class """
    def __init__(self, arg_file):
        self.file = arg_file

    def save_as(self, arg_new_file, arg_delimiter):
        """"Write file with new delimiter"""
        with open(self.file, 'r') as fr_handler:
            with open(arg_new_file, 'w', newline='') as fw_handler:
                csv_r = csv.reader(fr_handler)
                csv_w = csv.writer(fw_handler, delimiter=arg_delimiter)
                for line in csv_r:
                    csv_w.writerow(line)

    def sell_over(self, arg_product, arg_units_count):
        """" Return list of countries which have sold arg_product more than arg_units_count """
        with open(self.file, 'r') as fr_handler:
            csv_r = csv.reader(fr_handler)
            # Pass first line with headers
            next(csv_r)
            lst = [x[1] for x in csv_r if x[2] == arg_product and float(x[8]) > arg_units_count]
            # print(sorted(lst))
            return sorted(lst)

    def get_country_profit(self, arg_country):
        """" Return profit of country  """
        with open(self.file, 'r') as fr_handler:
            filtered_csv = (x for x in csv.DictReader(fr_handler) if x['Country'] == arg_country)
            profit = [float(x['Total Profit']) for x in filtered_csv]
            # print(sum(profit))
            return sum(profit)


if __name__ == "__main__":
    csv_parser = CsvParser('1000 Sales Records.csv')
    csv_parser.sell_over("Baby Food", 8000)
    csv_parser.get_country_profit('Nepal')
