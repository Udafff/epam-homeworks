def bold(dec_func):
    """Make input string bold"""
    def wrapper():
        return '<b>' + dec_func() + '</b>'
    return wrapper


if __name__ == "__main__":
    print('Message from bold decorator module!')
    pass
