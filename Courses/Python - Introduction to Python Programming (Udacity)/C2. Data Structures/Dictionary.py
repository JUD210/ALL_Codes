"""
[ Mutable , Insertion Ordered (python 3.6+) <- Unordered ]

ㅇStores mappings of unique keys to values.
ㅇNot even necessary for every key to have the same type.
ㅇKeys must be immutable.
Because keys are used to index values, they must be unique and immutable. For example, a string or tuple can be used as the key of a dictionary, but if you try to use a list as a key of a dictionary, you will get an error.

"""

elements = {'hydrogen': 1, 'helium': 2, 'carbon': 6}

x = elements.get('dilithium')
print('{} is None? {}'
      .format(x, x is None))
# None is None? True

x = elements.get('dilithium', 'default value')
print('{} is not None? {}'
      .format(x, x is not None))
# default value is None? True

# print(elements['dilithium'])
# KeyError: 'dilithium'


animals = {'dogs': [20, 10, 15, 8, 32, 15],
           'cats': [3, 4, 2, 8, 2, 4],
           'rabbits': [2, 3, 3],
           'fish': [0.3, 0.5, 0.8, 0.3, 1]}

print(animals.get('dogs')[:2])
# [20, 10]


""" Empty Dictionary """
a = {}
print("{} : {}".format(a, type(a)))

a = dict()
print("{} : {}".format(a, type(a)))
