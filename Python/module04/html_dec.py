def italic(dec_func):
    """Make input string italic"""
    def wrapper():
        return '<i>' + dec_func() + '</i>'
    return wrapper


def bold(dec_func):
    """Make input string bold"""
    def wrapper():
        return '<b>' + dec_func() + '</b>'
    return wrapper


def underline(dec_func):
    """Make input string underline"""
    def wrapper():
        return '<u>' + dec_func() + '</u>'
    return wrapper


# @underline
# @bold
# @italic
# def i_fun():
#     return 'Hello World'
#
#
# print(i_fun())
