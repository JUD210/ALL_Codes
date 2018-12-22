# https://www.hackerrank.com/challenges/py-if-else/problem


n = int(input())
# 5

result = ""
if n % 2 == 1:
    result += "Weird"
elif 2 <= n <= 5:
    result += "Not Weird"
elif 6 <= n <= 20:
    result += "Weird"
else:
    result += "Not Weird"

print(result)
# Weird
