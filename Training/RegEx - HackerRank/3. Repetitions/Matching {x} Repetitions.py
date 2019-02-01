# https://www.hackerrank.com/challenges/matching-x-repetitions/problem


import re

# Inputs
standard_input = """x4202v2A22A8a6aaaaaa2G2222m222qwertyYuIo139	7"""


Regex_Pattern = r"^[a-zA-Z02468]{40}[13579\s]{5}$"  # Do not delete 'r'.


print(str(bool(re.search(Regex_Pattern, input()))).lower())
# true
