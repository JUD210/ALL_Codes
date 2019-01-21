# https://www.hackerrank.com/challenges/validating-credit-card-number/problem?h_r=next-challenge&h_v=zen


import re


def card_validator(s):
    """ 
    ► It must start with a 4, 5 or 6. 
    ► It must contain exactly 16 digits. 
    ► It must only consist of digits (0-9). 
    ► It may have digits in groups of 4, separated by one hyphen "-". 
    ► It must NOT use any other separator like ' ' , '_', etc. 
    ► It must NOT have 4 or more consecutive repeated digits.
    """

    try:
        assert re.match(r"[456][\d]{3}-?[\d]{4}-?[\d]{4}-?[\d]{4}$", s)
        assert not re.search(r"(\d)(?:-?\1){3,}", s)

    except:
        return "Invalid"
    else:
        return "Valid"


for _ in range(int(input())):
    # 6
    s = input()
    # 4123456789123456
    # 5123-4567-8912-3456
    # 61234-567-8912-3456
    # 4123356789123456
    # 5133-3367-8912-3456
    # 5123 - 3567 - 8912 - 3456

    print(card_validator(s))

# Valid
# Valid
# Invalid
# Valid
# Invalid
# Invalid

