# https://runestone.academy/runestone/static/pythonds/AlgorithmAnalysis/Dictionaries.html


# |   Operation   |          Big-O Efficiency       |
# | ------------- | ------------------------------- |
# | copy          | O(n)                            |
# | get item      | O(1) (in some rare cases: O(n)) |
# | set item      | O(1) (in some rare cases: O(n)) |
# | delete item   | O(1)                            |
# | contains (in) | O(1) (in some rare cases: O(n)) |
# | iteration     | O(n)                            |

# The contains operator for lists is O(n) and the contains operator for dictionaries is O(1).


import timeit
import random  # noqa

print(f"i{'list'.rjust(15)}{'dict'.rjust(14)}")
print("==================================")
for i in range(100_000, 1_000_001, 200_000):
    t = timeit.Timer("random.randrange(%d) in x" % i, "from __main__ import random, x")

    x = list(range(i))  # type: ignore
    lst_time = t.timeit(number=1000)

    x = {j: None for j in range(i)}  # type: ignore
    d_time = t.timeit(number=1000)

    print("%d %10.3f ms %10.3f ms" % (i, lst_time, d_time))
# i           list          dict
# ==================================
# 100000      0.460 ms      0.001 ms
# 300000      1.326 ms      0.002 ms
# 500000      2.221 ms      0.001 ms
# 700000      3.489 ms      0.003 ms
# 900000      4.333 ms      0.001 ms
