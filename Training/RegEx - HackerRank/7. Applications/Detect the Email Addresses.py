# https://www.hackerrank.com/challenges/detect-the-email-addresses/problem


import re

# Inputs
standard_input = """14
Letters to the Editor (Your complete mailing address is required):
letters@thehindu.co.in
Readers' Editor:
readerseditor@thehindu.co.in
Advertisements Queries (Print):
inetads@thehindu.co.in
Advertisements Queries (Online):
digital@thehindu.co.in
Advertisements Queries (International):
international@thehindu.co.in
Subscription Queries:
subs@thehindu.co.in
Comments on the website:
web.thehindu@thehindu.co.in"""


emails = []
for _ in range(int(input())):

    line = input().strip()

    email_pattern = r"\w+(?:\.\w+)*@\w+(?:\.\w+)*"

    for found in re.findall(email_pattern, line):
        emails.append(found)


print(*sorted(set(emails), key=str), sep=";")

# digital@thehindu.co.in;inetads@thehindu.co.in;international@thehindu.co.in;letters@thehindu.co.in;readerseditor@thehindu.co.in;subs@thehindu.co.in;web.thehindu@thehindu.co.in
