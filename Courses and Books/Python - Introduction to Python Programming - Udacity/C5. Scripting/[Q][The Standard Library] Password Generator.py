import os, sys, inspect

# realpath() will make your script run, even if you symlink it :)
cmd_folder = os.path.realpath(
    os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe()))[0])
)

if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)

##### Above is not from this course.


""" Quiz: Password Generator

Write a function called generate_password that selects three random words from the list of words word_list and concatenates them into a single string. Your function should not accept any arguments and should reference the global variable word_list to build the password.
"""


# Use an import statement at the top
import random as rd


word_file_path = cmd_folder + "/Sub Files/words.txt"

# fill up the word_list
word_list = []
with open(word_file_path) as words:

    for line in words:
        # remove white space and make everything lowercase
        word = line.strip().lower()

        # don't include words that are too long or too short
        if 3 < len(word) < 8:
            word_list.append(word)

# Add your function generate_password here
# It should return a string consisting of three random words
# concatenated together without spaces
def generate_password():
    # result = ""
    # for i in range(3):
    #     result += rd.choice(word_list)
    # return result
    return ''.join(rd.sample(word_list, 3))
# test your function
print(generate_password())
