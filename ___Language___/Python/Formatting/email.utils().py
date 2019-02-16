import email.utils as eu

print(eu.parseaddr("DOSHI <DOSHI@hackerrank.com>"))
# ('DOSHI', 'DOSHI@hackerrank.com')
print(eu.formataddr(("DOSHI", "DOSHI@hackerrank.com")))
# DOSHI <DOSHI@hackerrank.com>

print(eu.parseaddr(("DOH! <S!@@@!!!@hacker!*%#.comma")))
# ('DOH!', 'S!@')
print(eu.formataddr(("DOH!", "<S!@@@!!!@hacker!*%#.comma")))
# DOH! <<S!@@@!!!@hacker!*%#.comma>

print(eu.parseaddr(("DOH! <d!#<>$%&*!@hacker!*%#.comma")))
# ('DOH!', 'd!#')
print(eu.formataddr(("DOH!", "d!#<>$%&*!@hacker!*%#.comma")))
# DOH! <d!#<>$%&*!@hacker!*%#.comma>