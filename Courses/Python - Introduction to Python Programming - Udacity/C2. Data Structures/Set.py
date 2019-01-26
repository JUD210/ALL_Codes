"""
[ Mutable, Unordered ]

ㅇApplication of a set is to quickly remove duplicates from a list.
"""

numbers = [1, 2, 6, 3, 1, 1, 6]
unique_nums = set(numbers)
print(unique_nums)
# {1, 2, 3, 6}


basket1 = {"apple", "banana"}
basket2 = {"apple", "watermelon", "kiwi"}

basket1.add("orange")

basket_union = basket1.union(basket2)
print(basket_union)
# {'banana', 'kiwi', 'watermelon', 'apple', 'orange'}

basket_intersection = basket1.intersection(basket2)
print(basket_intersection)
# {'apple'}

basket_difference = basket1.difference(basket2)
print(basket_difference)
# {'banana', 'orange'}
