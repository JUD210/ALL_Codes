# https://www.hackerrank.com/challenges/word-order/problem


d = dict()

for _ in range(int(input())):
    # 4
    s = input()
    d[s] = d.get(s, 0) + 1

# bcdef
# abcdefg
# bcde
# bcdef


print(len(d))
# 3
# 2 1 1
