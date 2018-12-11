""" Quiz: Extract First Names

Use a list comprehension to create a new list first_names containing just the first names in names in lowercase.
"""

names = [
    "Rick yick Rick Sanchez",
    "Morty Smith",
    "Summer Smith",
    "Jerry Smith",
    "Beth Smith",
]

# write your list comprehension here

first_names = [name.partition(" ")[0].lower() for name in names]
print(first_names)


"""  [Solution] """

# first_names = [name.split(" ")[0].lower() for name in names]
# print(first_names)
