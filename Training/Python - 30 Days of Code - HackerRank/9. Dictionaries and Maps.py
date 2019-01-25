# https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem


# Inputs
standard_input = """3
sam 99912222
tom 11122222
harry 12299933
sam
edwar
harry"""


""" Enter your code here. Read input from STDIN. Print output to STDOUT """


def create_contact():
    contact = {}
    for _ in range(n):
        input_data = input().split()
        contact[input_data[0]] = input_data[1]
    # sam 99912222
    # tom 11122222
    # harry 12299933

    return contact


def check_name(contact):
    for _ in range(n):
        name = input()
        # sam
        # edward
        # harry

        if name in contact:
            print(name + "=" + contact[name])
        else:
            print("Not found")


n = int(input())
# 3
contact = create_contact()
check_name(contact)
# sam=99912222
# Not found
# harry=12299933
