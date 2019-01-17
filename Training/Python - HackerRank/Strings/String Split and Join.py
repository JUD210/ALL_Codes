# https://www.hackerrank.com/challenges/python-string-split-and-join/problem


def split_and_join(line):
    return "-".join(line.split(" "))


line = input()
# this is a string   

result = split_and_join(line)
print(result)
# this-is-a-string
