"""
Slicing means using indices to slice off parts of an object like a string or a list.
"""


months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# List[Inclusive Index : Exclusive Index]

print(months)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(months[6:9])  # [7, 8, 9]
print(months[:3])  # [1, 2, 3]
print(months[9:])  # [10, 11, 12]
print(months[-3:])  # [10 ,11 ,12]
