# https://www.hackerrank.com/challenges/python-print/problem


import sys

n = int(input())

print(*list(range(1,n+1)), sep="", end="\n", file=sys.stdout, flush=False)