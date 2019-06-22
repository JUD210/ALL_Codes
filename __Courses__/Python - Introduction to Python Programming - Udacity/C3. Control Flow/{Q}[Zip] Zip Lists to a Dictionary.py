"""
Use zip to create a dictionary cast that uses names as keys and heights as values.
"""

cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]

cast = {}

# replace with your code
for temp in zip(cast_names, cast_heights):
    cast[temp[0]] = temp[1]

print(cast)