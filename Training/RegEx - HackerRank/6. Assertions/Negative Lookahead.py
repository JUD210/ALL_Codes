# https://www.hackerrank.com/challenges/negative-lookahead/problem


import re


# Inputs
standard_input = """###$$$$"""


Regex_Pattern = r"(.)(?!\1)"  # Do not delete 'r'.


Test_String = input()

match = re.findall(Regex_Pattern, Test_String)

print("Number of matches :", len(match))
# Number of matches : 2
