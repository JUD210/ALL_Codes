# https://www.hackerrank.com/challenges/py-collections-ordereddict/problem


from collections import OrderedDict

""" Note! ###############################################################

As of Python 3.6+, Dictionary is now Insertion Ordered.

Reference Below Sites

https://stackoverflow.com/questions/39980323/are-dictionaries-ordered-in-python-3-6?rq=1

https://mail.python.org/pipermail/python-dev/2017-December/151283.html

#########################################################################

dictionary = {}
dictionary["a"] = 1
dictionary["b"] = 2
dictionary["c"] = 3
dictionary["d"] = 4
dictionary["e"] = 5

print(dictionary)
# {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

ordered_dictionary = OrderedDict()
ordered_dictionary["a"] = 1
ordered_dictionary["b"] = 2
ordered_dictionary["c"] = 3
ordered_dictionary["d"] = 4
ordered_dictionary["e"] = 5

print(ordered_dictionary)
# OrderedDict([("a", 1), ("b", 2), ("c", 3), ("d", 4), ("e", 5)])

"""

d = dict()
# d = OrderedDict()

for _ in range(int(input())):
    # 9

    name, _, net_price = input().rpartition(" ")
    net_price = int(net_price)
    # s = input().split()
    # name, net_price = " ".join(s[:-1]), int(s[-1])

    # BANANA FRIES 12
    # POTATO CHIPS 30
    # APPLE JUICE 10
    # CANDY 5
    # APPLE JUICE 10
    # CANDY 5
    # CANDY 5
    # CANDY 5
    # POTATO CHIPS 30

    d[name] = d.get(name, 0) + net_price

for key, value in d.items():
    print(key, value)
    # BANANA FRIES 12
    # POTATO CHIPS 60
    # APPLE JUICE 20
    # CANDY 20
