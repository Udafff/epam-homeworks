"""
Module 06 - Log Parser
"""
import re


class LogParser:
    """ Log Parser class"""
    def __init__(self, arg_log_file):
        self.log_file = arg_log_file

    def get_most_common(self, arg_ip_count):
        """" Return top-'arg_ip_count' of IP addresses with the maximum number of request"""
        with open(self.log_file, 'r') as fr_handler:
            lst = []
            dct_ip = {ip.split(' ')[0]: 0 for ip in fr_handler if ip != '\n'}
            fr_handler.seek(0)
            for ip in fr_handler:
                if ip == '\n':
                    continue
                ip = ip.split(' ')[0]
                dct_ip.update({ip: int(dct_ip[ip]) + 1})

            for key, value in sorted(dct_ip.items(), key=lambda x: x[1], reverse=True):
                lst.append((key, value))

            # print(dct_ip)
            # print(lst[:arg_ip_count])
            return lst[:arg_ip_count]

    def log_by_http_code(self, arg_file_name, arg_response_number):
        """" Save to file entries filtered by server response """
        pattern = re.compile(rf'\s{arg_response_number}\s')
        with open(self.log_file, 'r') as fr_handler:
            with open(arg_file_name, 'w') as fw_handler:
                for line in fr_handler:
                    if pattern.search(line):
                        # print(line, end='')
                        fw_handler.write(line)


if __name__ == '__main__':
    print('Hello Gold')
    log_parser = LogParser('small_access.log')
    log_parser.get_most_common(4)
    log_parser.log_by_http_code('regexp_result.txt', 200)
