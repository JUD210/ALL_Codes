# https://dbader.org/blog/python-reverse-list


# Reversing a List In-Place With the  list.reverse() Method

""" 1 """
mylist = [1, 2, 3, 4, 5]
mylist.reverse()
print(mylist)
# [5, 4, 3, 2, 1]


""" 2 """
mylist = [1, 2, 3, 4, 5]
mylist = mylist[::-1]
print(mylist)
# [5, 4, 3, 2, 1]


""" 3 """
mylist = [1, 2, 3, 4, 5]
mylist = list(reversed(mylist))
print(mylist)
# [5, 4, 3, 2, 1]


""" + """
mylist = [1, 2, 3, 4, 5]
for item in reversed(mylist):
    print(item)
# 5
# 4
# 3
# 2
# 1

