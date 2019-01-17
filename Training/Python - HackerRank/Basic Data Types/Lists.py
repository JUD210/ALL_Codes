# https://www.hackerrank.com/challenges/python-lists/problem


num = int(input())
# 12


lst = []

for _ in range(num):
    cmd = input().strip().split()
    # insert 0 5
    # insert 1 10
    # insert 0 6
    # print
    # remove 6
    # append 9
    # append 1
    # sort
    # print
    # pop
    # reverse
    # print

    if cmd[0] == "insert":
        lst.insert(int(cmd[1]), int(cmd[2]))
    elif cmd[0] == "print":
        print(lst)
    elif cmd[0] == "remove":
        lst.remove(int(cmd[1]))
    elif cmd[0] == "append":
        lst.append(int(cmd[1]))
    elif cmd[0] == "sort":
        lst.sort()
    elif cmd[0] == "pop":
        lst.pop()
    elif cmd[0] == "reverse":
        lst.reverse()

    # insert i e: Insert integer  at position .
    # print: Print the list.
    # remove e: Delete the first occurrence of integer .
    # append e: Insert integer  at the end of the list.
    # sort: Sort the list.
    # pop: Pop the last element from the list.
    # reverse: Reverse the list.

# [6, 5, 10]
# [1, 5, 9, 10]
# [9, 5, 1]

