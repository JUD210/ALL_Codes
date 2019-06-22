# https://www.hackerrank.com/challenges/30-scope/problem


# Inputs
standard_input = """3
1 2 5"""


class Difference:
    def __init__(self, a):
        self.__elements = a

	# Add your code here
    def computeDifference(self):
        self.maximumDifference = max(self.__elements) - min(self.__elements)


# End of Difference class


_ = input()
# 3

a = [int(e) for e in input().split(' ')]
# 1 2 5

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
# 4
