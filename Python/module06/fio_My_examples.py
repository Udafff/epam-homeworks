from datetime import datetime
import csv


class FioTestExample:
    """"Test class for IO examples"""
    def __init__(self, arg_file):
        self.file = arg_file

    def main(self):
        pass
        # with open(filename) as file:
        #     lines = list(itertools.islice(file, 5, 9))
        #     sixth, ninth = lines[0], lines[3]

    def read_methods(self):
        f_handler = open(self.file, 'r')
        # Read first 1024 bytes of file and read the whole other part file to memory
        print(' First 1024 bytes:', f_handler.read(1024))
        print('\n Other part of file: ', f_handler.read())

        # Iteration method of reading file
        for ln in f_handler:
            print(ln)

        f_handler.close()

    def context_manager_io_read(self):
        """" Using context manager for file operations example """
        with open(self.file) as f_handle:
            for line in f_handle:
                print(line)

    def read_lines_methods(self):
        with open(self.file) as f_handler:
            # Read only one line in file and read whole file to memory and print()
            print('readline() - Read first one file line:', f_handler.readline())

            for line in f_handler.readlines():
                print('readlines() - Read all other lines:', line)

    # We use staticmethod, because we don't use Class Instance object
    @staticmethod
    def f_exception():
        """" IOError Exception handling """
        try:
            with open(r'NotExistFile.txt') as f_handler:
                pass
        except IOError as err:
            print("An IOError has occurred!")
            print(err)

    def write_methods(self):
        """" Write to file examples"""
        # Simple write a line of file to another one as byte stream
        with open(r'WriteToFile.txt', 'a') as f_write_handler:
            print(f'File {f_write_handler.name} is opened for writing with append')
            f_write_handler.write(f'{datetime.today().strftime("%d.%m.%Y, %H:%M")} : {open(self.file).readline()}')

    def file_pointer(self):
        """ Working with file pointer """
        with open(self.file)as f_handler:
            print('Read whole line: \n\t', f_handler.readline())
            f_handler.seek(0)

            print('Read first 6 bytes: \t\t\t', f_handler.read(6))
            print('  Position of pointer: \t\t\t', f_handler.tell())

            # Move pointer to the beginning of file
            print('\n# f_handler.seek(0)')
            f_handler.seek(0)

            print('Read 6 bytes more: \t\t\t\t', f_handler.read(6))
            print('Continue, Read 8 bytes: \t\t', f_handler.read(8))
            print('  Position of pointer: \t\t\t', f_handler.tell())
            print('Continue, Read 2 bytes: \t\t', f_handler.read(2))

            # Move pointer to 14
            print('\n# f_handler.seek(14)')
            f_handler.seek(14)

            print('Continue, Read 2 bytes more: \t', f_handler.read(2))

    def csv(self):
        with open(self.file) as f_handler:
            csv_r = csv.reader(f_handler)

            for line in csv_r:
                # print(line)
                print(line[0])

    def csv_writer(self):
        with open(self.file, 'r') as f_read_handler:
            with open('WriteToCSV.csv', "w", newline='') as f_write_handler:
                csv_r = csv.reader(f_read_handler)
                csv_w = csv.writer(f_write_handler, delimiter=';')

                for line in csv_r:
                    csv_w.writerow(line)

    def csv_dict_reader(self):
        """"csv OrderedDict"""
        with open(self.file) as f_handler:
            csv_dr = csv.DictReader(f_handler)
            for line in csv_dr:
                print(line)
                # print(line['Region'], '::', line['Item Type'])


if __name__ == "__main__":
    # print('Yellow gold!')
    fio = FioTestExample('1000 Sales Records.csv')

    # fio.main()
    # fio.read_methods()
    # fio.context_manager_io_read()
    # fio.read_lines_methods()

    # fio.f_exception()

    # fio.write_methods()

    # fio.file_pointer()

    # fio.csv_writer()
    fio.csv_dict_reader()

