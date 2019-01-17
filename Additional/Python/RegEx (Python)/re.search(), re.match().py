import re

""" 
The re.search() expression scans through a string looking for the first location where the regex pattern produces a match. 

It either returns a MatchObject instance or returns None if no position in the string matches the pattern.
"""

print(re.search(r"[a-c]+", "dabcdabcdabc"))
# <re.Match object; span=(1, 4), match='abc'>
print(re.search(r"[a-z]+", "abcdea"))
# <re.Match object; span=(0, 6), match='abcdea'>
print(bool(re.search(r"abc", "abcdea")))
# True

print(re.search(r"z", "similarly"))
# None
print(bool(re.search(r"z", "similarly")))
# False


""" 
The re.match() expression only matches at the beginning of the string. 

It either returns a MatchObject instance or returns None if the string does not match the pattern. 
"""

print(re.match(r"ly", "ly should be in the beginning"))
# <re.Match object; span=(0, 2), match='ly'>
print(bool(re.match(r"ly", "ly should be in the beginning")))
# True

print(re.match(r"ly", "similarly"))
# None
print(bool(re.match(r"ly", "similarly")))
# False
