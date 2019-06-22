# https://runestone.academy/runestone/static/pythonds/Introduction/ObjectOrientedProgramminginPythonDefiningClasses.html


def gcd(m, n):
    """
    Euclid's Algorithm
    """

    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn
    return n


class Fraction:
    def __init__(self, top, bottom):
        """
        Constructor (Initializer)
        """

        self.num = top  # numerator
        self.den = bottom  # denominator

    def __str__(self):
        """
        The print function requires that the object convert itself into a string so that the string can be written to the output.

        # print(super().__str__())
        # <__main__.Fraction object at 0x000002B122FDF908>
        """

        return f"{self.num}/{self.den}"

    def show(self):
        print(f"{self.num}/{self.den}")

    def __add__(self, other):
        """
        This solves below error.

        TypeError: unsupported operand type(s) for +:
                'instance' and 'instance'
        """

        newnum = self.num * other.den + self.den * other.num
        newden = self.den * other.den
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)

    def __eq__(self, other):
        """
        Two different objects with the same numerators and denominators would not be equal under default implementation. This is called shallow equality

        We can create deep equality equality by the same value, not the same reference by overriding the __eq__ method.

        It is important to note that there are other relational operators that can be overridden. For example, the __le__ method provides the less than or equal functionality.
        """

        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum == secondnum


f1 = Fraction(3, 5)
f2 = Fraction(1, 15)

print(f1.__str__())
# 3/5
print(f1)
# 3/5
f1.show()
# 3/5

print(f1.__add__(f2))
# 2/3
print(f1 + f2)
# 2/3


f3 = Fraction(3, 5)

print(f1 == f3)
# True  # Because we overrode __eq__ method.
