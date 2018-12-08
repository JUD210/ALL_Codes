# https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT


def create_contact():
    contact = {}
    for i in range(n):
        input_data = input().split()
        contact[input_data[0]] = input_data[1]

    return contact


def check_name(contact):
    for i in range(n):
        name = input()

        if name in contact:
            print(name + "=" + contact[name])
        else:
            print("Not found")


n = int(input())
contact = create_contact()
check_name(contact)
