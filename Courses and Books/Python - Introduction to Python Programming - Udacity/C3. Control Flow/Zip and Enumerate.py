""" Zip and Enumerate

zip and enumerate are useful built-in functions that can come in handy when dealing with loops.

    Zip

zip returns an iterator that combines multiple iterables into one sequence of tuples. Each tuple contains the elements in that position from all the iterables. 

For example, printing

list(zip(['a', 'b', 'c'], [1, 2, 3])) would output [('a', 1), ('b', 2), ('c', 3)].

Like we did for range() we need to convert it to a list or iterate through it with a loop to see the elements.

You could unpack each tuple in a for loop like this.

letters = ['a', 'b', 'c']
nums = [1, 2, 3]

for letter, num in zip(letters, nums):
    print("{}: {}".format(letter, num))


In addition to zipping two lists together, you can also unzip a list into tuples using an asterisk.

some_list = [('a', 1), ('b', 2), ('c', 3)]
letters, nums = zip(*some_list)


This would create the same letters and nums tuples we saw earlier.


    Enumerate

enumerate is a built in function that returns an iterator of tuples containing indices and values of a list. You'll often use this when you want the index along with each element of an iterable in a loop.

letters = ['a', 'b', 'c', 'd', 'e']
for i, letter in enumerate(letters):
    print(i, letter)

This code would output:

0 a
1 b
2 c
3 d
4 e 
"""

manifest = [
    ("bananas", 15),
    ("mattresses", 34),
    ("dog kennels", 42),
    ("machine", 120),
    ("cheeses", 5),
]

# This separate it into an items TUPLE and a weights TUPLE.
items, weights = zip(*manifest)
# is equal to below.
#
# items = 'bananas', 'mattresses', 'dog kennels', 'machine', 'cheeses'
# weights = 15, 34, 42, 120, 5


print("===")
print(items, weights)
# ('bananas', 'mattresses', 'dog kennels', 'machine', 'cheeses') (15, 34, 42, 120, 5)

print(manifest)
# [('bananas', 15), ('mattresses', 34), ('dog kennels', 42), ('machine', 120), ('cheeses', 5)]


print("===")
print(list(zip(items, weights)))
# [('bananas', 15), ('mattresses', 34), ('dog kennels', 42), ('machine', 120), ('cheeses', 5)]

print(zip(items, weights))
# <zip object at 0x00000250A9BEB208>


print("===")
for cargo in zip(items, weights):
    print(cargo[0], cargo[1])
# bananas 15
# mattresses 34
# dog kennels 42
# machine 120
# cheeses 5

print("===")
for item, weight in zip(items, weights):
    print(item, weight)
# bananas 15
# mattresses 34
# dog kennels 42
# machine 120
# cheeses 5


print("===")
for i, item in zip(range(len(items)), items):
    print(i, item)
# 0 bananas
# 1 mattresses
# 2 dog kennels
# 3 machine
# 4 cheeses

print("===")
for i, item in enumerate(items):
    print(i, item)
# 0 bananas
# 1 mattresses
# 2 dog kennels
# 3 machine
# 4 cheeses

print("===")
print(list(enumerate(items)))
# [(0, 'bananas'), (1, 'mattresses'), (2, 'dog kennels'), (3, 'machine'), (4, 'cheeses')]
