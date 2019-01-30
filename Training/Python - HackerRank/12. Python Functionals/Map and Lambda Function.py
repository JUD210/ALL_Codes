# https://www.hackerrank.com/challenges/map-and-lambda-expression/problem


def fibonacci(num):
    # return a list of fibonacci numbers
    # [0, 1, 1, 2, 3, 5, 8, 13, ...]

    lst = [0, 1]
    for _ in range(2, num):
        lst.append(lst[-1] + lst[-2])

    return lst[0:num]


if __name__ == "__main__":
    n = int(input())
    # 5

    print(list(map(lambda x: x ** 3, fibonacci(n))))
    # [0, 1, 1, 8, 27]
