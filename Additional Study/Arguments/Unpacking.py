# *args, **kwargs are called unpacking.
def save_ranking(*args, **kwargs):
    print(args)
    print(kwargs)


save_ranking("ming", "alice", "tom", test2="wilson", test1="roy")
# ('ming', 'alice', 'tom')
# {'test2': 'wilson', 'test1': 'roy'}


temp = [1, 2, "3", "4"]
print(temp)
# [1, 2, '3', '4']
print(*temp)
# 1 2 3 4

line = None
# to prevent below warning
# [use-before-def] 'line' used before definition


# *line = "1 2 3 4 5 6"
# SyntaxError: starred assignment target must be in a list or tuple

t1, t2, t3, *line = "1 2 3 4 5 6"
print(line)
# [' ', '3', ' ', '4', ' ', '5', ' ', '6']

t1, t2, t3, *line = "1 2 3 4 5 6".split()
print(line)
# ['4', '5', '6']
