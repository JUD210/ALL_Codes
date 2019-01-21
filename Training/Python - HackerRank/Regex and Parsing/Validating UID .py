# https://www.hackerrank.com/challenges/validating-uid/problem


import re


# """ Another Solution """"
def id_validator(s):
    """ A valid UID must follow the rules below:

    It must contain at least 2 uppercase English alphabet characters.
    It must contain at least 3 digits (0-9).
    It should only contain alphanumeric characters (a-z, A-Z & 0-9).
    No character should repeat.
    There must be exactly 10 characters in a valid UID.

    """
    try:
        s = ''.join(sorted(s))

        assert re.search(r"[A-Z]{2}", s)
        assert re.search(r"\d\d\d", s)
        assert not re.search(r"[^a-zA-Z0-9]", s)
        assert not re.search(r"(.)\1", s)
        assert len(s) == 10
    except:
        return "Invalid"
    else:
        return "Valid"


for _ in range(int(input())):
    # 2
    s = input()
    # B1CD102354
    # B1CDEF2354

    print(id_validator(s))
# Invalid   # B1CD102354 : 1 is repeating
# Valid


# """ My Solution """
def id_validator2(s):
    if len(s) == 10:
        if len(re.findall(r"[A-Z]", s)) >= 2:
            if len(re.findall(r"[0-9]", s)) >= 3:
                if re.match(r"[a-zA-Z0-9]+$", s):
                    if len(s) == len(set(s)):
                        return "Valid"

    return "Invalid"
