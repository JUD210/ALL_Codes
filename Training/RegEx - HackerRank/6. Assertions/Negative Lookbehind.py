# https://www.hackerrank.com/challenges/negative-lookbehind/problem


import re


# Inputs
standard_input = """1o1s"""


Regex_Pattern = r"(?<![aeiouAEIOU])."  # Do not delete 'r'.


Test_String = input()

match = re.findall(Regex_Pattern, Test_String)

print("Number of matches :", len(match))
# Number of matches : 3
