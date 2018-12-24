# https://www.hackerrank.com/challenges/string-validators/problem


s = input().strip()
# qA2

print(any([c.isalnum() for c in s]))
# True
print(any([c.isalpha() for c in s]))
# True
print(any([c.isdigit() for c in s]))
# True
print(any([c.islower() for c in s]))
# True
print(any([c.isupper() for c in s]))
# True
