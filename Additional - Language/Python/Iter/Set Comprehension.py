words = "This is a sample text".split()


length = set()
for word in words:
    length.add(len(word))
print(length)
# [4, 2, 1, 6, 4]

print({len(word) for word in words})
# [4, 2, 1, 6, 4]

print({len(word) for word in words if len(word) > 3})
# [4, 6, 4]
