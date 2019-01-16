# https://www.hackerrank.com/challenges/py-introduction-to-sets/problem


def average(array):
    array = set(array)
    return sum(array) / len(array)


if __name__ == "__main__":
    n = int(input())
    # 10   # len(arr)

    arr = list(map(int, input().split()))
    # 161 182 161 154 176 170 167 171 170 174

    result = average(arr)
    print(result)
    # 169.375
