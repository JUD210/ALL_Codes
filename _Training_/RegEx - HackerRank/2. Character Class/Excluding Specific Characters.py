# https://www.hackerrank.com/challenges/excluding-specific-characters/problem


import re


# Inputs
standard_input = """think?"""

Regex_Pattern = (
    r"^[^\d][^aeiou][^bcDF][^\r\n\t\f\s][^AEIOU][^.,]$"
)  # Do not delete 'r'.

print(str(bool(re.search(Regex_Pattern, input()))).lower())
# true
