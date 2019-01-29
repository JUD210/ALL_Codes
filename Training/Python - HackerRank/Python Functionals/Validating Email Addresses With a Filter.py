# https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter/problem


import re


""" Not Using Regex """


def fun(email):
    # return True if s is a valid email, else return False

    # It must have the username@websitename.extension format type.
    # The username can only contain letters, digits, dashes and underscores.
    # The website name can only have letters and digits.
    # The maximum length of the extension is .
    try:
        username, url = email.split("@")
        website, extension = url.split(".")
    except ValueError:
        return False

    if not username.replace("-", "").replace("_", "").isalnum():
        return False
    if not website.isalnum():
        return False
    if len(extension) > 3:
        return False
    return True


""" Using Regex """


def fun2(email):
    a = re.match(r"[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$", email)
    # {1,3}: The last part of the regex[a-zA-Z] must have a length between 1~3
    # $: Returns None if no extension exists
    return a


def filter_mail(emails):
    return list(filter(fun, emails))


if __name__ == "__main__":
    n = int(input())
    # 3

    emails = []
    for _ in range(n):
        emails.append(input())
    # lara@hackerrank.com
    # brian-23@hackerrank.com
    # britts_54@hackerrank.com

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
# ['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']
