# https://www.hackerrank.com/challenges/positive-lookbehind/problem


import re


# Inputs
standard_input = """123Go!"""


Regex_Pattern = r"(?<=[13579])\d"  # Do not delete 'r'.

Test_String = input()

match = re.findall(Regex_Pattern, Test_String)

print("Number of matches :", len(match))
# Number of matches : 1
