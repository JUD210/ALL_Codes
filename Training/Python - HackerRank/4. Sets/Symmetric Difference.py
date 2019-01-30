# https://www.hackerrank.com/challenges/symmetric-difference/problem


s1, s2 = [set(input().split()) for _ in range(4)][1::2]
# 4   # len(s1)
# 2 4 5 9
# 4   # len(s2)
# 2 4 11 12


# A u B - A n B
print("\n".join(sorted(s1.union(s2).difference(s1.intersection(s2)), key=int)))
# print("\n".join(sorted(s1 ^ s2, key=int)))
# print(*sorted(s1 ^ s2, key=int), sep="\n")
# 5
# 9
# 11
# 12

""" My First Answer

n1_len, n1 = int(input()), set(map(int, input().split()))
n2_len, n2 = int(input()), set(map(int, input().split()))

"""
