# https://www.hackerrank.com/challenges/30-linked-list-deletion/problem


# Inputs
standard_input = """6
4
2
1
3
4
2"""

# !TODO: Study Again!


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def insert(self, head, data):
        p = Node(data)
        if head is None:
            head = p
        elif head.next is None:
            head.next = p
        else:
            start = head
            while start.next is not None:
                start = start.next
            start.next = p
        return head

    def display(self, head):
        current = head
        while current:
            print(current.data, end=" ")
            current = current.next

    def remove_duplicates(self, head):
        # Write your code here
        current = head
        while current:

            checker = current.data
            subcurrent = current
            while subcurrent.next:
                if subcurrent.next.data == checker:
                    subcurrent.next = subcurrent.next.next
                    continue
                subcurrent = subcurrent.next

            current = current.next

        return head


mylist = Solution()
T = int(input())
# 6

head = None
for i in range(T):
    data = int(input())
    # 4
    # 2
    # 1
    # 3
    # 4
    # 2

    head = mylist.insert(head, data)
head = mylist.remove_duplicates(head)
mylist.display(head)
# 4 2 1 3
