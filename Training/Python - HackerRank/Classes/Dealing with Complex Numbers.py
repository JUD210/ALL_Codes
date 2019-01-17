# https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers/problem


""" My Answer """

import math


class Complex(object):
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        # (1+2i)(3+4i) = (1*3) + {(1*4)+(2*3)}i + (2*4)(-1)
        return Complex(
            self.real * other.real - self.imag * other.imag,
            self.real * other.imag + self.imag * other.real,
        )

    def __truediv__(self, other):
        # (3+2i)/(4-3i)
        # = (3+2i)*(4+3i)/(4-3i)*(4+3i)
        # = 6+7i / 25
        # = 6/25 + 7i/25
        numerator = self * Complex(other.real, -other.imag)
        denominator = (other * Complex(other.real, -other.imag)).real
        return Complex(numerator.real / denominator, numerator.imag / denominator)

    def mod(self):
        return Complex(math.sqrt(pow(self.real, 2) + pow(self.imag, 2)), 0)

    def __str__(self):
        return "{0.real:.2f}{0.imag:+.2f}i".format(self)


""" Solution 2 """


class Complex2(complex):
    def __add__(self, no):
        return Complex2(complex.__add__(self, no))

    def __sub__(self, no):
        return Complex2(complex.__sub__(self, no))

    def __mul__(self, no):
        return Complex2(complex.__mul__(self, no))

    def __truediv__(self, no):
        return Complex2(complex.__truediv__(self, no))

    def mod(self):
        return Complex2(complex.__abs__(self))

    def __str__(self):
        return "{0.real:.2f}{0.imag:+.2f}i".format(self)


if __name__ == "__main__":
    c = map(float, input().split())
    d = map(float, input().split())
    # 11 19
    # -11 -19
    x = Complex(*c)
    y = Complex(*d)
    print(x, y, sep="\n")
    print(*map(str, [x + y, x - y, x * y, x / y, x.mod(), y.mod()]), sep="\n")

# 0.00+0.00i
# 22.00+38.00i
# 240.00-418.00i
# -1.00+0.00i
# 21.95+0.00i
# 21.95+0.00i

