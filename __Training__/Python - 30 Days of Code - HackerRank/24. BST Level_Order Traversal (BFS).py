# https://www.hackerrank.com/challenges/30-binary-trees/problem


# Inputs
standard_input = """6
3
5
4
7
2
1"""

# !TODO: Study Again!


class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data


class Solution:
    def insert(self, root, data):
        if root is None:
            return Node(data)
        else:
            if data <= root.data:
                current = self.insert(root.left, data)
                root.left = current
            else:
                current = self.insert(root.right, data)
                root.right = current
        return root

    def level_order(self, root):
        # Write your code here
        queue = [root] if root else []
        while queue:
            current = queue.pop()
            print(current.data, end=" ")

            if current.left:
                queue.insert(0, current.left)
            if current.right:
                queue.insert(0, current.right)


T = int(input())
# 6

myTree = Solution()

root = None
for i in range(T):
    data = int(input())
    # 3
    # 5
    # 4
    # 7
    # 2
    # 1

    root = myTree.insert(root, data)
myTree.level_order(root)

# 3 2 5 1 4 7


#    3
#  2/ \5
# 1/ 4/ \7
#
# 3-2-5-1-4-7
