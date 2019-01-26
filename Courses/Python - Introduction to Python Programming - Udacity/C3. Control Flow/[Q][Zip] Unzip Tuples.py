""" Unzip the cast tuple into two names and heights tuples.
"""

cast = (("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76))

# define names and heights here
names, heights = zip(*cast)

print(names)
# ('Barney', 'Robin', 'Ted', 'Lily', 'Marshall')
print(heights)
# (72, 68, 72, 66, 76)
print(list(zip(*cast)))
# [('Barney', 'Robin', 'Ted', 'Lily', 'Marshall'), (72, 68, 72, 66, 76)]