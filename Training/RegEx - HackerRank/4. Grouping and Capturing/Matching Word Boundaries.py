# https://www.hackerrank.com/challenges/matching-word-boundaries/problem


import re


# Inputs
standard_input = """Found any match?"""


Regex_Pattern = r"\b[aeiouAEIOU][a-zA-Z]*\b"  # Do not delete 'r'.

# Three different positions qualify for word boundaries :
# : Before the first character in the string, if the first character is a word character.
# : Between two characters in the string, where one is a word character and the other is not a word character.
# : After the last character in the string, if the last character is a word character.


print(str(bool(re.search(Regex_Pattern, input()))).lower())
# true
