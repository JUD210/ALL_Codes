"""
Slicing means using indices to slice off parts of an object like a string or a list.
"""


months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# List[Start(Inclusive) : End(Exclusive) : Step]

print(months)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(months[:])
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(months[::])
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

print(months[6:9])
# [7, 8, 9]
print(months[:3])
# [1, 2, 3]
print(months[9:])
# [10, 11, 12]

print(months[-4:])
# [9, 10 ,11 ,12]

print(months[::2])
# [1, 3, 5, 7, 9, 11]
print(months[::-1])
# [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

print(months [5:10:2])
# [6, 8, 10]