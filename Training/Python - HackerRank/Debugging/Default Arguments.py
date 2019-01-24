# https://www.hackerrank.com/challenges/default-arguments/problem


# Inputs
standard_input = """3
odd 2
even 3
odd 5"""


class EvenStream(object):
    def __init__(self):
        self.current = 0

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return


class OddStream(object):
    def __init__(self):
        self.current = 1

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return


# FIX THIS!
# def print_from_stream(n, stream=EvenStream()):
#     for _ in range(n):
#         print(stream.get_next())
def print_from_stream(n, stream=None):
    if stream is None:
        stream = EvenStream()
    for _ in range(n):
        print(stream.get_next())


queries = int(input())
# 3

for _ in range(queries):
    stream_name, n = input().split()
    # odd 2
    # even 3
    # odd 5
    n = int(n)
    if stream_name == "even":
        print_from_stream(n)
    else:
        print_from_stream(n, OddStream())

# 1
# 3
# 0
# 2
# 4
# 1
# 3
# 5
# 7
# 9
