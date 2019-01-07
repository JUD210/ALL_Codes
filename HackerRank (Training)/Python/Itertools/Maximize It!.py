# https://www.hackerrank.com/challenges/maximize-it/problem


from itertools import product

"""
given f(X) = X^2

given K lists.
The i th list consists of N_i elements.

X_i denotes the element picked from the i th list.
S = (f(X_1) + f(X_2) + ... + f(X_k)) % M

1 <= K <= 7
1 <= N_i <= 7
1 <= M <= 1000
1 <= Magnitude of elements in list <= 10^9

Maximum S value : ?

"""

K, M = map(int, input().split())
# 7 952

N = (list(map(int, input().split()))[1:] for _ in range(K))
# 6 386364143 56297585 479292050 782778989 177771725 945191156
# 7 458982242 957774948 25202756 357554307 248513713 506622954 769577156
# 3 109432676 494972174 914814315
# 1 49979276
# 2 491584479 103564062
# 1 25883738
# 1 460971693

results = map(lambda x: sum(i ** 2 for i in x) % M, product(*N))
print(max(results))
# 943

""" My Answer

k = []

len_k, m = map(int, input().split())
# 7 952
for _ in range(len_k):
    k.append(list(map(int, input().split()[1:])))
    # 6 386364143 56297585 479292050 782778989 177771725 945191156
    # 7 458982242 957774948 25202756 357554307 248513713 506622954 769577156
    # 3 109432676 494972174 914814315
    # 1 49979276
    # 2 491584479 103564062
    # 1 25883738
    # 1 460971693

tuples = [tpl for tpl in product(*k)]

s = []
for t in tuples:

    result = 0
    for i in range(len(t)):
        result += t[i] ** 2
    result = result % m
    s.append(result)

print(max(s))
# print(k, sum(k[0]))
# 943

"""
