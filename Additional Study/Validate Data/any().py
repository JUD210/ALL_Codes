""" any() returns:

True if at least one element of an iterable is true
False if all elements are false or if an iterable is empty

"""

# All values are True
l = [1, 2, 3]
print(any(l))
# True

# One value is False (others are True)
l = [1, 2, 0]
print(any(l))
# True

# One value is True (others are False)
l = [1, 0, 0]
print(any(l))
# True


# All values are False
l = [0, 0, 0]
print(any(l))
# False

# Empty Iterable
l = []
print(any(l))
# False
