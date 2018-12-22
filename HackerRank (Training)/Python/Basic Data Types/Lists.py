# https://www.hackerrank.com/challenges/python-lists/problem


num = int(input())

lst = []

for _ in range(num):
    cmd = input().strip().split()

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
