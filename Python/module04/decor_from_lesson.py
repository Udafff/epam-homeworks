"""
LEGB
Local, Enclosing, Global, Built-In
Decoration Demonstration from lesson
"""

from datetime import datetime
from functools import wraps
from time import sleep

#### Example 1
print('========= Example 1')


def my_decorator(func):
    print('Come to decor=', func)

    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Params came to wrapper()=', args, kwargs)

        print("This executed before function: {}".format(func.__name__))

        result_of_execution = func(*args, **kwargs)
        print('Result of func exec=', result_of_execution)

        print("This executed after function: {}".format(func.__name__))
        return result_of_execution
    return wrapper


@my_decorator
def my_f(a, b):
    print('Func begin:')
    print('', a)
    print('', b)
    return 'Function execute complete'


my_f("A", "B")


#### Example 2
print()
print('========= Example 2')


def my_timer(msg):
    # Executed only in @decorator init before function
    print('## Begin my_timer Decorator creator')
    print('   Come to Decor creator arg: msg=', msg)

    def decorator(func):
        print('   Come to decorator arg=', func)

        def wrapper(*args, **kwargs):
            print('#### Begin wrapper')
            print('     Params came to wrapper, *args, **kwarg=', args, kwargs)

            t1 = datetime.now()
            res = func(*args, **kwargs)
            print("{} {}".format(msg, datetime.now() - t1))
            return res
        return wrapper

    print('   Decorator created, return decorator=', decorator)

    return decorator


@my_timer("Execution took: ")
def test_2(msg):
    """This function returns Hello world"""
    sleep(1)
    return msg


@my_timer("BlaBlaBla: ")
def test(msg):
    """This function returns Hello world"""
    sleep(1)
    return msg


test("Function: test")
test_2("Function: test_2")
