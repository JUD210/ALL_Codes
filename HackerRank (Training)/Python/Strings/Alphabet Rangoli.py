# https://www.hackerrank.com/challenges/alphabet-rangoli/problem


def print_rangoli(size):

    chars = []
    for ascii_add in range(size - 1, -(size - 1) - 1, -1):
        # ascii_add : 4 3 2 1 0-1-2-3-4

        if ascii_add >= 0:
            chars.append(chr(ord("a") + ascii_add))
        elif ascii_add < 0:
            chars.pop()

        new_chars = chars[:] + chars[-2::-1]

        print("-".join(new_chars).center(size * 4 - 3, "-"))

    # --------e--------
    # ------e-d-e------
    # ----e-d-c-d-e----
    # --e-d-c-b-c-d-e--
    # e-d-c-b-a-b-c-d-e
    # --e-d-c-b-c-d-e--
    # ----e-d-c-d-e----
    # ------e-d-e------
    # --------e--------


if __name__ == "__main__":
    num = int(input())
    # 5

    print_rangoli(num)
