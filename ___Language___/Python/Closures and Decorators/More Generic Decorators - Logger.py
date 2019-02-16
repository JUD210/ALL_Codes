# http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/


def logger(func):
    def inner(*args, **kwargs):  # 1
        print(f"[logger's inner] args:{args}, kwargs:{kwargs}")

        return func(*args, **kwargs)  # 2

    return inner


@logger
def multiply(x, multi=5, **kwargs):
    print(f"[multiply] kwargs:{kwargs}, kwargs.values():{kwargs.values()}")
    return (x + sum(kwargs.values())) * multi


@logger
def return_2():
    return 2


print(multiply(5, 4))
# [logger's inner] args:(5, 4), kwargs:{}
# [multiply] kwargs:{}, kwargs.values():dict_values([])
# 20

print(multiply(3, four=4, five=5))
# [logger's inner] args:(3,), kwargs:{'four': 4, 'five': 5}
# [multiply] kwargs:{'four': 4, 'five': 5}, kwargs.values():dict_values([4, 5])
# 60

print(multiply(3, four=4, five=5, multi=100))
# [logger's inner] args:(3,), kwargs:{'four': 4, 'five': 5, 'multi': 100}
# [multiply] kwargs:{'four': 4, 'five': 5}, kwargs.values():dict_values([4, 5])
# 1200

print(return_2())
# [logger's inner] args:(), kwargs:{}
# 2
