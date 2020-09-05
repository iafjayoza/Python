# Decorators can be used to change the behaviour of existing function at compile time

#Example 1
def div(a,b):
    print(a/b)

def smart_div(func):
    def inner(a,b):
        if a < b:
            a,b =b,a
        return func(a,b)
    return inner


div = smart_div(div)
div(2,4)

#Example 2

def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print("Wrapper function executed before {} function".format(original_function.__name__))
        return original_function(*args, **kwargs)

    return wrapper_function


@decorator_function
def display():
    print("Display function ran")


@decorator_function
def display_info(name, age):
    print("{0} is {1} years old".format(name, age))


display()

display_info("Jay", 27)


