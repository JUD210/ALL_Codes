"""
len()
max()
min()
sorted()
append()
pop()
"""

fruits = ['banana', 'kiwi', 'apple', 'watermelon']

print(len(fruits))  # 4

print(max(fruits))  # watermelon
print(min(fruits))  # apple

fruits.append('strawberry')

print(sorted(fruits))
# ['apple', 'banana', 'kiwi', 'strawberry', 'watermelon']

print(fruits.pop())  # strawberry
print(fruits.pop())  # watermelon
print(fruits.pop())  # apple
print(fruits.pop())  # kiwi
print(fruits.pop())  # banana
# print(fruits.pop())
# IndexError: pop from empty list