# @decorator parameter
def raises(decor_param):
    # Function for decoration
    def decorator(decorated_func):
        # Wrapper for function
        # Can be with arguments of function: def wrapper(*args, **kwargs)
        def wrapper():
            try:
                decorated_func()
            except Exception:
                raise decor_param
        return wrapper
    return decorator


if __name__ == "__main__":
    print('Message from raises decorator module!')
    pass
