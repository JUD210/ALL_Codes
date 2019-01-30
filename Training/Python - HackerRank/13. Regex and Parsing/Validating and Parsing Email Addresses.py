# https://www.hackerrank.com/challenges/validating-named-email-addresses/problem


"""
import email.utils

print(email.utils.parseaddr("DOSHI <DOSHI@hackerrank.com>"))
# ('DOSHI', 'DOSHI@hackerrank.com')
print(email.utils.formataddr(("DOSHI", "DOSHI@hackerrank.com")))
# DOSHI <DOSHI@hackerrank.com>

print(email.utils.parseaddr(("DOH! <S!@@@!!!@hacker!*%#.comma")))
# ('DOH!', 'S!@')
print(email.utils.formataddr(("DOH!", "<S!@@@!!!@hacker!*%#.comma")))
# DOH! <<S!@@@!!!@hacker!*%#.comma>

"""


"""
1. Try using Email.utils() to complete this challenge.

2. A valid email address meets the following criteria:

    * It's composed of a username, domain name, and extension assembled in this format: username@domain.extension

    * The username starts with an English alphabetical character, and any subsequent characters consist of one or more of the following: alphanumeric characters, -,., and _.

    * The domain and extension contain only English alphabetical characters.

    * The extension is 1, 2, or 3 characters in length.

"""


### Using email.utils
import re, email.utils

for _ in range(int(input())):
    # 2
    s = input()
    # DEXTER <dexter@hotmail.com>
    # VIRUS <virus!@variable.:p>

    try:
        nickname, full = email.utils.parseaddr(s)
        # ('DEXTER', '<dexter@hotmail.com>')
        username, temp = full.split("@")
        # ['dexter', 'hotmail.com']
        domain, extension = temp.split(".")
        # ['hotmail', 'com']

        if re.match(r"[a-zA-Z][\w\-_.]*$", username):
            if re.match(r"[a-zA-Z]+$", domain):
                if re.match(r"[a-zA-Z]{1,3}$", extension):
                    print(s)
                    # DEXTER <dexter@hotmail.com>
    except:
        continue



### Using regex ONLY
import re

for _ in range(int(input())):
    x, y = input().split(' ')
    
    m = re.match(r'<[A-Za-z][\w\-_.]+@[A-Za-z]+\.[A-Za-z]{1,3}>', y)
    if m:
        print(x,y)