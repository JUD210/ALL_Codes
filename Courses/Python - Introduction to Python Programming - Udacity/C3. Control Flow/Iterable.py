""" iterable

An Object that can return one of its elements at a time

This can include sequence types such as strings, lists, and tuples as well as non-sequenced types such as dictionaries and files.

You can define objects within iter method to allow them to be used as an iterable.


for city in cities:
    print(city.title())

for: Signals that this is a for loop.
city: The iteration variable.
cities: The iterable being looped over.

"""