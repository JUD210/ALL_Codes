# https://www.hackerrank.com/challenges/map-and-lambda-expression/problem


# complete the lambda function
cube = lambda x: x ** 3


def fibonacci(num):
    # return a list of fibonacci numbers
    # [0, 1, 1, 2, 3, 5, 8, 13, ...]

    l = [0, 1]
    for _ in range(2, num):
        l.append(l[-1] + l[-2])

    return l[0:num]


if __name__ == "__main__":
    n = int(input())
    # 5

    print(list(map(cube, fibonacci(n))))
    # [0, 1, 1, 8, 27]
