# https://www.hackerrank.com/challenges/30-binary-search-trees/problem


# Inputs
standard_input = """7
3
5
2
1
4
6
7"""

# !TODO: Study Again!


class Node:
    def __init__(self, data):
        self.data = data
        self.right = self.left = None


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

    def get_height2(self, root):
        if root is None or (root.left is None and root.right is None):
            return 0
        else:
            return max(self.get_height(root.left), self.get_height(root.right)) + 1

    def get_height(self, root):
        # Write your code here
        if root:
            left_depth = self.get_height(root.left)
            right_depth = self.get_height(root.right)

            # print(
            #     f"root.data={root.data}, left_depth={left_depth}, right_depth={right_depth}"
            # )
            # root.data=1, left_depth=-1, right_depth=-1
            # root.data=2, left_depth=0, right_depth=-1
            # root.data=4, left_depth=-1, right_depth=-1
            # root.data=7, left_depth=-1, right_depth=-1
            # root.data=6, left_depth=-1, right_depth=0
            # root.data=5, left_depth=0, right_depth=1
            # root.data=3, left_depth=1, right_depth=2

            return max(left_depth, right_depth) + 1
        else:
            return -1


T = int(input())
# 7

myTree = Solution()
root = None
for i in range(T):
    data = int(input())
    # 3
    # 5
    # 2
    # 1
    # 4
    # 6
    # 7

    root = myTree.insert(root, data)
height = myTree.get_height(root)
print(height)
# 3

#    3
#  2/ \5
# 1/ 4/ \6
#         \7
