# https://www.hackerrank.com/challenges/validating-postalcode/problem


""" A valid postal code have to fullfil both below requirements:

It must be a number in the range from 100000 to 999999 inclusive.
It must not contain more than one alternating repetitive digit pair.

"""

regex_integer_in_range = r"[1-9]\d{5}$"
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"
110000

import re
P = input()

print (bool(re.match(regex_integer_in_range, P))
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)