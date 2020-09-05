# Class Decorators
import time
from functools import wraps

class decorator_class(object):
    def __init__(self,original_function):
        self.original_function = original_function
    def __call__(self, *args, **kwargs):
        print("Call method executed this before {}".format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)



@decorator_class
def display():
    print("Display function ran")

@decorator_class
def display_info(name,age):
    print( "{0} is {1} years old".format(name,age))

# display()
# display_info("Jay",27)

# Functional Decorator

def my_logger(original_function):
    import logging
    logging.basicConfig(filename='{}.log'.format(original_function.__name__),level= logging.INFO)

    @wraps(original_function)
    def wrapper_function(*args, **kwargs):
        logging.info("Ran with args {} and kwargs {}".format(args,kwargs))
        return original_function(*args, **kwargs)

    return wrapper_function


def my_timer(original_function):
    import time

    @wraps(original_function)
    def wrapper_function(*args, **kwargs):
        t1 = time.time()
        result = original_function(*args, **kwargs)
        t2 = time.time() - t1
        print("{} ran in {} seconds".format(original_function.__name__,t2))
        return result

    return wrapper_function

# @my_logger
# def display_info(name, age):
#     print("{0} is {1} years old".format(name, age))
#
# @my_timer
# def display_info(name, age):
#     time.sleep(1)
#     print("{0} is {1} years old".format(name, age))

@my_logger
@my_timer
def display_info(name, age):
    time.sleep(1)
    print("{0} is {1} years old".format(name, age))


display_info("Madhavi", 22)

