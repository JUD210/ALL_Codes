# https://www.hackerrank.com/challenges/collections-counter/problem


from collections import Counter

"""
s = "daaababcc"
# result is same with
# s = ['d','a','a','a','b','a','b','c','c']

print(Counter(s))
# Counter({'a': 4, 'b': 2, 'c': 2, 'd': 1})

print(Counter(s).items())
# dict_items([('d', 1), ('a', 4), ('b', 2), ('c', 2)])

print(Counter(s).keys())
# dict_keys(['d', 'a', 'b', 'c'])

print(Counter(s).values())
# dict_values([1, 4, 2, 2])

print(Counter(s).most_common())
# [('a', 4), ('b', 2), ('c', 2), ('d', 1)]

print(Counter(s).most_common(2))
# [('a', 4), ('b', 2)]

"""



num_shoes, sizes = int(input()), Counter(map(int, input().split()))
# 10
# 2 3 4 5 6 8 7 6 5 18

# print(sizes)
# Counter({5: 2, 6: 2, 2: 1, 3: 1, 4: 1, 8: 1, 7: 1, 18: 1})

num_customers = int(input())
# 6

income = 0
for _ in range(num_customers):
    size, price = map(int, input().split())
    # 6 55
    # 6 45
    # 6 55
    # 4 40
    # 18 60
    # 10 50

    if sizes[size]:
        income += price
        sizes[size] -= 1


print(income)
# 200
