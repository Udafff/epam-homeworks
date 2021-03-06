from functools import wraps


def delay(d_fun):
    """Sleep decorator"""
    @wraps(d_fun)
    def wrapper():
        import time
        time.sleep(3)
        d_fun()
    return wrapper
