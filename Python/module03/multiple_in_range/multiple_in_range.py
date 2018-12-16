def multiple_in_range(st_range, en_range):
    try:
        return [i for i in range(st_range, en_range + 1) if i % 7 == 0 and i % 5 > 0]
    except TypeError:
        raise TypeError
