"""
is
: evaluates if both sides have the same identity

is not
: evaluates if both sides have different identity
"""

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a == b)  # True
print(a is b)  # True
print(a == c)  # True
print(a is c)  # False


b[2] = 9

print(a)  # [1, 2, 9]
print(b)  # [1, 2, 9]
print(c)  # [1, 2, 3]
