""" Quiz: Verse Dictionary

In the code editor below, you'll find a dictionary containing the unique words of verse stored as keys and the number of times they appear in verse stored as values. Use this dictionary to answer the following questions. Submit these answers in the quiz below the code editor.

Try to answer these using code, rather than inspecting the dictionary manually!

1. How many unique words are in verse_dict?
2. Is the key "breathe" in verse_dict?
3. What is the first element in the list created when verse_dict is sorted by keys?
    Hint: Use the appropriate dictionary method to get a list of its keys, and then sort that list. Use this list of keys to answer the next two questions as well.
4. Which key (word) has the highest value in verse_dict?
"""

verse_dict = {'if': 3, 'you': 6, 'can': 3, 'keep': 1, 'your': 1, 'head': 1, 'when': 2, 'all': 2, 'about': 2, 'are': 1, 'losing': 1, 'theirs': 1, 'and': 3, 'blaming': 1, 'it': 1, 'on': 1, 'trust': 1, 'yourself': 1, 'men': 1, 'doubt': 1, 'but': 1, 'make': 1, 'allowance': 1, 'for': 1, 'their': 1,
              'doubting': 1, 'too': 3, 'wait': 1, 'not': 1, 'be': 1, 'tired': 1, 'by': 1, 'waiting': 1, 'or': 2, 'being': 2, 'lied': 1, 'don\'t': 3, 'deal': 1, 'in': 1, 'lies': 1, 'hated': 1, 'give': 1, 'way': 1, 'to': 1, 'hating': 1, 'yet': 1, 'look': 1, 'good': 1, 'nor': 1, 'talk': 1, 'wise': 1}
print(verse_dict, '\n')

# find number of unique keys in the dictionary
num_keys = len(verse_dict)
print(num_keys)


# find whether 'breathe' is a key in the dictionary
contains_breathe = 'breathe' in verse_dict
# contains_breathe = verse_dict.get('breathe')

print(contains_breathe)


# create and sort a list of the dictionary's keys
sorted_keys = sorted(verse_dict.keys())


# get the first element in the sorted list of keys

# print(sorted_keys)
# ['about', 'all', 'allowance', 'and', 'are', 'be', 'being', 'blaming', 'but', 'by', 'can', 'deal', "don't", 'doubt', 'doubting', 'for', 'give', 'good', 'hated', 'hating', 'head', 'if', 'in', 'it', 'keep', 'lied', 'lies', 'look', 'losing', 'make', 'men', 'nor', 'not', 'on', 'or', 'talk', 'their', 'theirs', 'tired', 'to', 'too', 'trust', 'wait', 'waiting', 'way', 'when', 'wise', 'yet', 'you', 'your', 'yourself']

print(sorted_keys[0])


# find the element with the highest value in the list of keys
# meaning alphabetical value.

print(sorted_keys[-1])

# Don't be confused with below
# print(max(sorted_keys))
