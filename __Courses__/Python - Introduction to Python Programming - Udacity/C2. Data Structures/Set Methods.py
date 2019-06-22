"""
add()
pop()
union()
intersection()
difference()
"""

fruit = {"apple", "banana", "orange"}
fruit.add("watermelon")
print(fruit.pop())
# Remove a random element and print it.
fruit.pop()
# Remove a random element

basket1 = {"apple", "banana", "orange"}
basket2 = {"apple", "watermelon", "kiwi"}



basket_union = basket1.union(basket2)
print(basket_union)
# {'banana', 'kiwi', 'watermelon', 'apple', 'orange'}

basket_intersection = basket1.intersection(basket2)
print(basket_intersection)
# {'apple'}

basket_difference = basket1.difference(basket2)
print(basket_difference)
# {'banana', 'orange'}