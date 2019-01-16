# https://www.hackerrank.com/challenges/reduce-function/problem


from fractions import Fraction
from functools import reduce


def product(fracs):
    # complete this line with a reduce statement
    t = reduce(lambda x, y: x * y, fracs)
    return t.numerator, t.denominator


if __name__ == "__main__":

    fracs = []
    for _ in range(int(input())):
        # 3
        fracs.append(Fraction(*map(int, input().split())))
    # 1 2
    # 3 4
    # 10 6

    result = product(fracs)
    print(*result)
    # 5 8
