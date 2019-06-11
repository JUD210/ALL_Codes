# https://www.hackerrank.com/challenges/hackerrank-tweets/problem


import re


# Inputs
standard_input = """4
I love #hackerrank
I just scored 27 points in the Picking Cards challenge on #HackerRank
I just signed up for summer cup @hackerrank
interesting talk by hari, co-founder of hackerrank"""


count = 0
for _ in range(int(input())):
    line = input().strip().lower()

    if re.search("hackerrank", line):
        count += 1

print(count)
# 4
