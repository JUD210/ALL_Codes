"""
[ Mutable, Ordered ]

Can contain any type of object.

"""

fruits = ['banana', 'kiwi', 'apple', 'watermelon']

print(fruits)
# ['banana', 'kiwi', 'apple', 'watermelon']
print(sorted(fruits))
# ['apple', 'banana', 'kiwi', 'watermelon']


mixed = [True, 1, "Ya", 'ho']

print(mixed)
# [True, 1, 'Ya', 'ho']

print(mixed[0])
# True

# print(sorted(mixed))
# TypeError: '<' not supported between instances of 'str' and 'int'
