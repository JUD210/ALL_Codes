# https://www.hackerrank.com/challenges/whats-your-name/problem


def print_full_name(a, b):
    print("Hello " + a + " " + b + "! You just delved into python.")
    # Hello Ross Taylor! You just delved into python.


if __name__ == "__main__":
    first_name = input()
    # Ross
    last_name = input()
    # Taylor

    print_full_name(first_name, last_name)
