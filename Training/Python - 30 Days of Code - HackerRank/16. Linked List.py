# https://www.hackerrank.com/challenges/30-linked-list/problem


# Inputs
standard_input = """4
2
3
4
1"""

# TODO: Study Again Later


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def display(self, head):
        current = head

        while current:
            print(current.data, end=" ")
            current = current.next

    def insert(self, head, data):
        if head == None:
            head = Node(data)
        elif head.next == None:
            head.next = Node(data)
        else:
            self.insert(head.next, data)
        return head


mylist = Solution()

T = int(input())
# 4

head = None
for i in range(T):
    data = int(input())
    # 2
    # 3
    # 4
    # 1

    head = mylist.insert(head, data)

mylist.display(head)
# 2 3 4 1
