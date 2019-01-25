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

# TODO: Study Again Later


class Node:
    def __init__(self, data):
        self.data = data
        self.right = self.left = None


class Solution:
    def insert(self, root, data):
        if root == None:
            return Node(data)
        else:
            if data <= root.data:
                current = self.insert(root.left, data)
                root.left = current
            else:
                current = self.insert(root.right, data)
                root.right = current
        return root

    def getHeight2(self, root):
        if root is None or (root.left is None and root.right is None):
            return 0
        else:
            return max(self.getHeight(root.left), self.getHeight(root.right)) + 1

    def getHeight(self, root):
        # Write your code here
        if root:
            leftDepth = self.getHeight(root.left)
            rightDepth = self.getHeight(root.right)

            # print(
            #     f"root.data={root.data}, leftDepth={leftDepth}, rightDepth={rightDepth}"
            # )
            # root.data=1, leftDepth=-1, rightDepth=-1
            # root.data=2, leftDepth=0, rightDepth=-1
            # root.data=4, leftDepth=-1, rightDepth=-1
            # root.data=7, leftDepth=-1, rightDepth=-1
            # root.data=6, leftDepth=-1, rightDepth=0
            # root.data=5, leftDepth=0, rightDepth=1
            # root.data=3, leftDepth=1, rightDepth=2

            return max(leftDepth, rightDepth) + 1
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
height = myTree.getHeight(root)
print(height)
# 3

#    3
#  2/ \5
# 1/ 4/ \6
#         \7
