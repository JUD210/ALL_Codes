# Quiz: Fruit Basket

# You would like to count the number of fruits in your basket.
# In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number
# of fruits and not_fruits.

basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

# Iterate through the dictionary
fruit_count, not_fruit_count = 0, 0
for item, ea in basket_items.items():

    # if the key is in the list of fruits, add to fruit_count.
    if item in fruits:
        fruit_count += ea

    # if the key is not in the list, then add to the not_fruit_count
    else:
        not_fruit_count += ea

print("The number of fruits is {}.\nThere are {} items that are not fruits.".format(
    fruit_count, not_fruit_count))
