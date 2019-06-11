# https://www.hackerrank.com/challenges/re-findall-re-finditer/problem


import re

#   """ re.findall()
#
#   The expression re.findall() returns all the non-overlapping matches of patterns in a string as a list of strings.
#
#   """
#   print(re.findall(r"\w", "http://www.hackerrank.com/"))
#   # ['h', 't', 't', 'p', 'w', 'w', 'w', 'h', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k', 'c', 'o', 'm']
#
#
#   """ re.finditer()
#
#   The expression re.finditer() returns an iterator yielding MatchObject instances over all non-overlapping matches for the re pattern in the string.
#
#   """
#
#   print(re.finditer(r"\w", "http://www.hackerrank.com/"))
#   # <callable-iterator object at 0x0266C790>
#   print(list(map(lambda x: x.group(), re.finditer(r"\w", "http://www.hackerrank.com/"))))
#   # ['h', 't', 't', 'p', 'w', 'w', 'w', 'h', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k', 'c', 'o', 'm']


""" My Answer """

import re

re_vowels = r"[AEIOUaeiou]"
re_consonants = r"[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]"

s = input()
# rabcdeefgyYhFjkIoomnpOeorteeeeet

m = re.findall(
    rf"(?<={re_consonants}){re_vowels}" + "{2,}" + rf"(?={re_consonants})", s
)
print("\n".join(m) if m else -1)

# ee        # is located between consonant d and f.
# Ioo       # is located between consonant k and m.
# Oeo       # is located between consonant p and r.
# eeeee     # is located between consonant t and t.
