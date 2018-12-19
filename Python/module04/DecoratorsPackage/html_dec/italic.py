def italic(dec_func):
    """Make input string italic"""
    def wrapper():
        return '<i>' + dec_func() + '</i>'
    return wrapper


if __name__ == "__main__":
    print('Message from italic decorator module!')
    pass
