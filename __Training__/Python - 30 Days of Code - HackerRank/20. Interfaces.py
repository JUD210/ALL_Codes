# https://www.hackerrank.com/challenges/30-interfaces/problem


# Inputs
standard_input = """6"""


class AdvancedArithmetic(object):
    def divisorSum(self, n):
        raise NotImplementedError


class Calculator(AdvancedArithmetic):
    # Write your code here
    def divisorSum(self, n1):
        return sum([n2 for n2 in range(1, n1 + 1) if n1 % n2 == 0])
        # sum([1, 2, 3, 6]) == 12

n = int(input())
# 6

my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)
# I implemented: AdvancedArithmetic
# 12
