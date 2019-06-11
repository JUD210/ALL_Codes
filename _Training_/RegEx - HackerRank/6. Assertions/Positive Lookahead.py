# https://www.hackerrank.com/challenges/positive-lookahead/problem


import re


# Inputs
standard_input = """gooooo!"""


Regex_Pattern = r"o(?=oo)"  # Do not delete 'r'.


Test_String = input()

match = re.findall(Regex_Pattern, Test_String)

print("Number of matches :", len(match))
# Number of matches : 3
