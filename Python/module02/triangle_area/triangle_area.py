import sys

if __name__ == "__main__":
    if len(sys.argv) != 1:
        print('Incorrect number of parameters')
        sys.exit(1)


def triangle_area(a, b, c):
    try:
        if a > b + c or b > a + c or c > a + b:
            print('Triangle edges are not correct!')
            raise ValueError

        if a + b == c or b + c == a or a + c == b:
            print('Non-zero scalar')
            raise ValueError

        p = (a + b + c) / 2
        s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        print('The area of a triangle:', s)
        return 0
    except TypeError:
        # print('TypeError!!!')
        sys.exit(1)
        # raise TypeError
    except ValueError:
        # print('ValueError!!!')
        sys.exit(1)
        # raise ValueError


try:
    triangle_area(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]))
except TypeError:
    print('TypeError!!!')
    # raise TypeError
except ValueError:
    print('ValueError!!!')
    # raise ValueError
