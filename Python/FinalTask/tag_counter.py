""" Final task - tag counter
    python ./tag_counter.py -h
    python ./tag_counter.py -m url 'https://yandex.ru'
    python ./tag_counter.py -m file html_file.html
    python ./tag_counter.py -l file -m url 'https://yandex.ru'
    python ./tag_counter.py -l aws -m url 'https://google.com'
"""
import requests
import sys
from bs4 import BeautifulSoup
import logging
import argparse
import boto3


class TagCounter:
    def __init__(self):
        """ Class initialization """
        self.total_tags = 0
        self.tags_dict = {}
        # Logging mode (Disabled, file, aws)
        self.log = ['Disabled', "tag_counter.log"]

    def count(self, arg_mode, arg_source):
        """" Main Class method.
            arg_mode = 'url' - Get HTML page from arg_source URL.
            arg_mode = 'file' - Read HTML file from arg_source file name.
            arg_mode = 'html' - Parse plain text HTML string from arg_source String Object.
            Write result in a file
            Return a list [total_tags, tags_dictionary]"""
        source_is = arg_source
        if arg_mode == 'url':
            self.count_tags(self.html_from_url(arg_source))
        elif arg_mode == 'file':
            self.count_tags(self.html_from_file(arg_source))
        elif arg_mode == 'html':
            self.count_tags(arg_source)
            source_is = 'HtmlText'

        # Write to log file
        if self.log[0] != 'Disabled':
            self.write_log([self.log[0], self.log[1], source_is])

        return [source_is, self.total_tags, self.tags_dict]

    def config_log(self,arg_log_params):
        """ Reconfigure logging """
        self.log = arg_log_params
        # Remove all handlers associated with the root logger object.
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)
        # Reconfigure logging with a file and write to log file.
        logging.basicConfig(filename=arg_log_params[1], level=logging.INFO, format='%(asctime)s %(message)s')
        if arg_log_params[0] == 'aws':
            logging.getLogger('botocore').setLevel(logging.ERROR)

    def write_log(self, arg_log_params):
        """ Get a list of params and write data to log:
            arg_log_params[0] - Type of log (file|aws or "Disabled")
            arg_log_params[1] - Log filename
            arg_log_params[2] - Html source (url|file|HtmlText)"""

        if arg_log_params[0] == 'file':
            logging.info(f'"{arg_log_params[2]}" {self.total_tags} {self.tags_dict}')
        elif arg_log_params[0] == 'aws':
            s3 = boto3.resource('s3')
            logging.info(f'"{arg_log_params[2]}" {self.total_tags} {self.tags_dict}')
            # aws uploading
            if s3.Bucket('tag-counter') in s3.buckets.all():
                s3.Bucket('tag-counter').upload_file(arg_log_params[1], arg_log_params[1])
            else:
                print(f'The specified bucket does not exist. Please create a bucket with name "tag-counter".')
        else:
            print(f'Log destination: "{arg_log_params[0]}" is incorrect. It have to be "file" or "aws" or "Disabled".')

    @staticmethod
    def html_from_url(arg_url):
        """ Make a request to URL, get Plain HTML text and return a string with it.  """
        try:
            response = requests.get(arg_url, headers={"Accept-Language": "En-us"})
            return response.text
        except requests.exceptions.ConnectionError as err:
            print('ConnectionError:', err)
            logging.info(f'ConnectionError:{err}')
            sys.exit(1)
        except requests.exceptions.MissingSchema as err:
            print('Invalid URL:', err)
            logging.info(f'Invalid URL:{err}')
            sys.exit(1)
        except requests.exceptions.InvalidSchema as err:
            print('Invalid URL:', err)
            logging.info(f'Invalid URL:{err}')
            sys.exit(1)

    @staticmethod
    def html_from_file(arg_file_name):
        """" Read Plain HTML text from file and return a string with it. """
        try:
            with open(arg_file_name, 'r') as file_handler:
                return file_handler.read()
        except IOError as err:
            print('IOError:', err)
            logging.info(f'IOError:{err}')
            sys.exit(1)

    def count_tags(self, arg_plain_html):
        """ Main count method. Parse string with HTML text,
            count tags and update total_tags, tags_dict Class Instance variables """
        tags_soup = BeautifulSoup(arg_plain_html, 'lxml').findAll()
        self.total_tags = 0
        self.tags_dict = {tag.name: 0 for tag in tags_soup}

        # Update tag Dictionary and count tags
        for tag in tags_soup:
            self.tags_dict.update({tag.name: int(self.tags_dict[tag.name] + 1)})
            self.total_tags += 1


if __name__ == "__main__":
    """ Main program """
    # Configure Argument Parser options
    parser = argparse.ArgumentParser(description='#### Count html tags in object (URL, File). ####')
    parser.add_argument('source', metavar='SOURCE', help='Source of html data \
                        ("https://www.google.com", "html_file.html").')
    parser.add_argument('-m', help='Source mode [url|file].', choices=['url', 'file'], required=True)
    parser.add_argument('-l', help='Enable logging.', choices=['file', 'aws'])
    args = parser.parse_args()

    # Create class instance
    cls_count_tags = TagCounter()

    # Enable logging
    if args.l == 'file':
        cls_count_tags.config_log(['file', 'tag_counter_file.log'])
    elif args.l == 'aws':
        cls_count_tags.config_log(['aws', 'tag_counter_aws.log'])

    # Execute and print result
    if args.m == 'url':
        result = cls_count_tags.count('url', args.source)
        print(f'Source: {result[0]}\nTotal tags: {result[1]}')
        for tag in result[2].items():
            print(f'{tag[0]}:{tag[1]}')
    elif args.m == 'file':
        result = cls_count_tags.count('file', args.source)
        print(f'Source: {result[0]}\nTotal tags: {result[1]}')
        for tag in result[2].items():
            print(f'{tag[0]}:{tag[1]}')
