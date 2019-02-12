lst = ["1", "100", 63, "4", 2, "900", 0]
print(sorted(lst, key=str))
# [0, '1', '100', 2, '4', 63, '900']

lst.sort(key=int)  # type: ignore
print(lst)
# [0, '1', 2, '4', 63, '100', '900']

lst = [int(n) for n in lst]  # type: ignore
print(lst)
# [0, 1, 2, 4, 63, 100, 900]


###################


def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]


people = [
    ["Mike", "Thomson", "20", "M"],
    ["Robert", "Bustle", "32", "M"],
    ["Andria", "Bustle", "30", "F"],
]

result = [name_format(person) for person in sorted(people, key=lambda p: p[2])]
### sorting key = age

print(*result, sep="\n")
# Mr. Mike Thomson
# Ms. Andria Bustle
# Mr. Robert Bustle
