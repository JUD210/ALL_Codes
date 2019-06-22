"""
ㅇIf a single argument (object) is passed to type() built-in, it returns type of the given object.

ㅇIf three arguments (name, bases and dict) are passed, it returns a new type object.
"""

print(type(4))  # <class 'int'>
print(type(4.))  # <class 'float'>
print(type(4.0))  # <class 'float'>

x = .1+.1+.1
print(x)  # 0.30000000000000004

y = .3
print(y)  # 0.3

print(x == y)  # False

print(type(x == y))  # <class 'bool'>
