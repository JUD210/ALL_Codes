# https://www.hackerrank.com/challenges/finding-the-percentage/problem


n = int(input())
student_marks = {}

for _ in range(n):

    name, *scores = input().split()
    scores = list(map(float, scores))
    student_marks[name] = sum(scores)/len(scores)
    
query_name = input()

print("{:.2f}".format(student_marks[query_name]))
