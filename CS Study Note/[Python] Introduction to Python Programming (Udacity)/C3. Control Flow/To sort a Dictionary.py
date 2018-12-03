""" http://code.activestate.com/recipes/52306-to-sort-a-dictionary/

Dictionaries can't be sorted -- a mapping has no ordering! -- so, when you feel the need to sort one, you no doubt want to sort its keys (in a separate list). Sorting (key,value) pairs (items) is simplest, but not fastest.
"""

# (IMHO) the simplest approach:
def sortedDictValues1(adict):
    items = adict.items()
    items.sort()
    return [value for key, value in items]


# an alternative implementation, which
# happens to run a bit faster for large
# dictionaries on my machine:
def sortedDictValues2(adict):
    keys = adict.keys()
    keys.sort()
    return [dict[key] for key in keys]


# a further slight speed-up on my box
# is to map a bound-method:
def sortedDictValues3(adict):
    keys = adict.keys()
    keys.sort()
    return map(adict.get, keys)
