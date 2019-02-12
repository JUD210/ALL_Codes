""" http://code.activestate.com/recipes/52306-to-sort-a-dictionary/

Dictionaries can't be sorted -- a mapping has no ordering! -- so, when you feel the need to sort one, you no doubt want to sort its keys (in a separate list). Sorting (key,value) pairs (items) is simplest, but not fastest.
"""

# (IMHO) the simplest approach:
def sortedDictValues1(adict):
    items = adict.items()
    items = sorted(items)
    return [value for key, value in items]


# an alternative implementation, which
# happens to run a bit faster for large
# dictionaries on my machine:
def sortedDictValues2(adict):
    keys = adict.keys()
    keys = sorted(keys)
    return [adict[key] for key in keys]


# a further slight speed-up on my box
# is to map a bound-method:
def sortedDictValues3(adict):
    keys = adict.keys()
    keys = sorted(keys)
    return list(map(adict.get, keys))


d = {5: 50, 2: 20, 3: 30}

print(sortedDictValues1(d))
print(sortedDictValues2(d))
print(sortedDictValues3(d))
# [20, 30, 50]
# [20, 30, 50]
# [20, 30, 50]
