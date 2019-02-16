# prevent use-before-def
rest, line = None, None

""" Simple Examples of Unpacking """
numbers = [1, 2, "3", "4"]
print(numbers)
# [1, 2, '3', '4']
print(*numbers)
# 1 2 3 4

numbers = [1, 2, "3", "4"]
one, *rest = numbers
print(one)
# 1
print(rest)
# [2, '3', '4']

# *numbers
# SyntaxError: starred assignment target must be in a list or tuple


"""
var_1, var_2, *var_rest = iterable
var_1 = iterable[0]
var_2 = iterable[1]
var_rest = iterable[2:]

"""

tpl = t1, t2, t3, *line = "1 2 3 4 5 6"
print(tpl)
# 1 2 3 4 5 6
print(t1, t2, t3)
# 1   2
print(line)
# [' ', '3', ' ', '4', ' ', '5', ' ', '6']

tpl = t1, t2, t3, *line = "1 2 3 4 5 6".split()  # type: ignore
print(tpl)
# ['1', '2', '3', '4', '5', '6']
print(t1, t2, t3)
# 1 2 3
print(line)
# ['4', '5', '6']


""" *args, **kwargs are called unpacking too. """


def save_ranking(*args, **kwargs):
    # Variable name 'args' or 'kwargs' doesn't matter.
    print(args)
    print(kwargs)


save_ranking("ming", "alice", "tom", test2="wilson", test1="roy")
# ('ming', 'alice', 'tom')
# {'test2': 'wilson', 'test1': 'roy'}
