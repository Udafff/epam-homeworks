def underline(dec_func):
    """Make input string underline"""
    def wrapper():
        return '<u>' + dec_func() + '</u>'
    return wrapper


if __name__ == "__main__":
    print('Message from underline decorator module!')
    pass
