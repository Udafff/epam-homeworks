def raises(d_fun):
    def wrapper(*args):
        try:
            return 0
        except Exception:
            raise args
    return wrapper

