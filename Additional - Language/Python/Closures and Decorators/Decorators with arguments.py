# https://www.codementor.io/moyosore/a-dive-into-python-closures-and-decorators-part-2-ab2enoyjg


""" 
Remember a decorator is a callable function, this make it possible for us to pass in arguments to our decorators. Arguments are passed into decorators same way it can be passed into normal functions.


# Parsing arguments to a normal fuction

normal_function(arg1, arg2)
normal_function(arg1="Hello", arg2="Dear")


# Passing arguments into a decorator

@my_decorator(arg1, arg2)
def my_function():
    pass


@my_decorator(arg1="Hello", arg2="World")
def my_function():
    pass
"""

##################################


def decorator(arg1, arg2):
    def main_decorator(func):
        def func_wrapper(*args, **kwargs):
            f = func(*args, **kwargs)
            return f"Hi {f}, {arg1} {arg2}"

        return func_wrapper

    return main_decorator


@decorator("hello", "dear")
def my_function(name):
    return name


print(my_function("Emma"))  
# 'Hi Emma, hello dear'


#######################################


def greet_speaker(time="day"):
    print(time.lower())

    def greet_decorator(func):
        def greet_person(name):
            if name == "Josh":
                return f"Good {time}, !{func(name)}!"
            else:
                return f"Good {time}, {name}"

        return greet_person

    return greet_decorator


@greet_speaker()
def greet1(name):
    return name.upper()


@greet_speaker("Morning")
def greet2(name):
    return name.upper()


@greet_speaker(time="Evening")
def greet3(name):
    return name.upper()


# day
# morning
# evening
print(greet1("Josh"))  # Good day !JOSH!
print(greet2("Aduke"))  # Good Morning Aduke
print(greet3("Chima"))  # Good Evening Chima
