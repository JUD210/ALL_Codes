# https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators/problem


import re


""" Solution """


def wrapper(f):
    def formattor(l):
        f(["+91 " + phone[-10:-5] + " " + phone[-5:] for phone in l])

    return formattor


""" My Solution Using RegEx """


def wrapper2(f):
    def formattor(l):
        """
        The given mobile numbers may have +91, 91 or 0 written before the actual 10 digit number. Alternatively, there may not be any prefix at all. 

        """
        new_l = []
        for phone in l:

            if len(phone) == 10:
                phone = "+91" + phone
            elif len(phone) == 12:
                phone = re.sub(r"(?<=^)91", "+91", phone)
            elif len(phone) == 11:
                phone = re.sub(r"(?<=^)0", "+91", phone)

            phone = re.sub(r"(\+\d{2})(\d{5})(\d{5})", r"\1 \2 \3", phone)

            new_l.append(phone)
        return f(new_l)

    return formattor


@wrapper
def sort_phone(l):
    print(*sorted(l), sep="\n")


if __name__ == "__main__":
    l = [input() for _ in range(int(input()))]
    # 3

    # 07895462130
    # 919875641230
    # 9195969878

    sort_phone(l)
    # +91 78954 62130
    # +91 91959 69878
    # +91 98756 41230

