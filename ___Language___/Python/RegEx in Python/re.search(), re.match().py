# https://www.hackerrank.com/challenges/introduction-to-regex/problem


import re

""" re.search()

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


""" re.match()

The re.match() expression only matches at the beginning of the string. 

It either returns a MatchObject instance or returns None if the string does not match the pattern. 

"""

print(re.match(r"ly", "ly should be in the beginning"))
# <re.Match object; span=(0, 1), match='ly'>
print(bool(re.match(r"ly", "ly should be in the beginning")))
# True

print(re.match(r"ly", "similarly"))
# None
print(bool(re.match(r"ly", "similarly")))
# False


for case in ["a", "abc", "aaaaabc", "b", "ba"]:
    print(f"{case}\t\tpattern : 'a'\t\t\t{bool(re.match(r'a', case))}")
    print(f"{case}\t\tpattern : 'a$'\t\t\t{bool(re.match(r'a$', case))}")
    print(f"{case}\t\tpattern : ' '\t\t\t{bool(re.match(r' ', case))}")
    print(
        f"{case}\t\tpattern : '(?:b{0,1}|z)'\t{bool(re.match(r'(?:b{0,2}|z)', case))}"
    )
    print(
        f"{case}\t\tpattern : '(?:b{0,1}|z)$'\t{bool(re.match(r'(?:b{0,2}|z)$', case))}"
    )
    print("")

# a               pattern : 'a'                   True
# a               pattern : 'a$'                  True
# a               pattern : ' '                   False
# a               pattern : '(?:b(0, 1)|z)'       True
# a               pattern : '(?:b(0, 1)|z)$'      False

# abc             pattern : 'a'                   True
# abc             pattern : 'a$'                  False
# abc             pattern : ' '                   False
# abc             pattern : '(?:b(0, 1)|z)'       True
# abc             pattern : '(?:b(0, 1)|z)$'      False

# aaaaabc         pattern : 'a'                   True
# aaaaabc         pattern : 'a$'                  False
# aaaaabc         pattern : ' '                   False
# aaaaabc         pattern : '(?:b(0, 1)|z)'       True
# aaaaabc         pattern : '(?:b(0, 1)|z)$'      False

# b               pattern : 'a'                   False
# b               pattern : 'a$'                  False
# b               pattern : ' '                   False
# b               pattern : '(?:b(0, 1)|z)'       True
# b               pattern : '(?:b(0, 1)|z)$'      True

# ba              pattern : 'a'                   False
# ba              pattern : 'a$'                  False
# ba              pattern : ' '                   False
# ba              pattern : '(?:b(0, 1)|z)'       True
# ba              pattern : '(?:b(0, 1)|z)$'      False
