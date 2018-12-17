import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Incorrect number of parameters')
        sys.exit(1)


def is_interval(digit):
    try:
        if (-15 < digit <= 12) or (14 < digit < 17) or (digit >= 19):
            # print(digit)
            print('True')
            return 0
        else:
            # print(digit)
            print('False')
            return 1
    except ValueError:
        print('TypeError!!!')
        sys.exit(1)


try:
    is_interval(float(sys.argv[1]))
except ValueError:
    print('ValueError!!!')
    # raise ValueError
    sys.exit(1)
