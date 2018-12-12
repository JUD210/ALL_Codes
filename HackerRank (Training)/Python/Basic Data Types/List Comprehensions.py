# https://www.hackerrank.com/challenges/list-comprehensions/problem

x = int(input())
y = int(input())
z = int(input())

n = int(input())

# Condition
# 1. lexicographic increasing order.
# 2. i+j+k != n

dimensions = []

for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if i+j+k != n:
                dimensions.append([i, j, k])

# dimensions = [[i,j,k for i in range(x+1)], 

print(dimensions)


# Multiples of 3 below 10
ListOfThreeMultiples = [x for x in range(10) if x % 3 == 0] 
print(ListOfThreeMultiples)