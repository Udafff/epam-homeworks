import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Incorrect number of parameters')
        sys.exit(1)


def multiplier_case(str_data):
    try:
        print(str_data)
        return 0

    except ValueError:
        print('TypeError!!!')
        sys.exit(1)


try:
    if any(i.isdigit() for i in sys.argv[1]):
        print('Arg. include digit!')
        raise ValueError
    str_res = ''.join(str(i).upper() + str(i * index).lower() + '-' for index, i in enumerate(sys.argv[1]))[:-1]
    print(str_res)
except ValueError:
    print('ValueError!!!')
    # raise ValueError
    sys.exit(1)
