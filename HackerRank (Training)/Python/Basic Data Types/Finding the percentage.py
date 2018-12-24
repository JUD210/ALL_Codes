# https://www.hackerrank.com/challenges/finding-the-percentage/problem


n = int(input())
# 3

student_marks = {}

for _ in range(n):

    name, *scores = input().split()
    # Krishna 67 68 69
    # Arjun 70 98 63
    # Malika 52 56 60

    scores = list(map(float, scores))
    student_marks[name] = sum(scores) / len(scores)

query_name = input()
# Malika

print("{:.2f}".format(student_marks[query_name]))
# 56.00
