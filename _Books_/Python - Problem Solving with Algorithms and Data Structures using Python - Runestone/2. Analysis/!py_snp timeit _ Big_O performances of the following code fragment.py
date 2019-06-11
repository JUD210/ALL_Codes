# https://runestone.academy/runestone/static/pythonds/AlgorithmAnalysis/DiscussionQuestions.html


import timeit

# flake8: noqa
# pylint: disable=unused-variable


def test1(n):
    for i in range(n):
        for j in range(n):
            k = 2 + 2


def test2(n):
    for i in range(n):
        k = 2 + 2


def test3(n):
    i = n
    while i > 0:
        k = 2 + 2
        i = i // 2


def test4(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                k = 2 + 2


def test5(n):
    for i in range(n):
        k = 2 + 2
    for j in range(n):
        k = 2 + 2
    for k in range(n):
        k = 2 + 2


results = {}  # type: ignore
results["t1"] = []
results["t2"] = []
results["t3"] = []
results["t4"] = []
results["t5"] = []
for i in range(10, 101, 10):
    print(i)

    t1 = timeit.Timer(f"test1({i})", "from __main__ import test1")
    results["t1"].append(f"i: {i}  " + str(t1.timeit(number=1000).__round__(6)) + " ms")
    t2 = timeit.Timer(f"test2({i})", "from __main__ import test2")
    results["t2"].append(f"i: {i}  " + str(t2.timeit(number=1000).__round__(6)) + " ms")
    t3 = timeit.Timer(f"test3({i})", "from __main__ import test3")
    results["t3"].append(f"i: {i}  " + str(t3.timeit(number=1000).__round__(6)) + " ms")
    t4 = timeit.Timer(f"test4({i})", "from __main__ import test4")
    results["t4"].append(f"i: {i}  " + str(t4.timeit(number=1000).__round__(6)) + " ms")
    t5 = timeit.Timer(f"test5({i})", "from __main__ import test5")
    results["t5"].append(f"i: {i}  " + str(t5.timeit(number=1000).__round__(6)) + " ms")


print("\n=== Result ===")
print("Test 1: O(n^2)\n" + "\n".join(results["t1"]) + "\n")
print("Test 2: O(n)\n" + "\n".join(results["t2"]) + "\n")
print("Test 3: O(n)\n" + "\n".join(results["t3"]) + "\n")
print("Test 4: O(n^3)\n" + "\n".join(results["t4"]) + "\n")
print("Test 5: O(n)\n" + "\n".join(results["t5"]) + "\n")

# 10
# 20
# 30
# 40
# 50
# 60
# 70
# 80
# 90
# 100
#
# === Result ===
# Test 1: O(n^2)
# i: 10  0.005112 ms
# i: 20  0.010765 ms
# i: 30  0.031468 ms
# i: 40  0.028105 ms
# i: 50  0.042794 ms
# i: 60  0.080282 ms
# i: 70  0.081793 ms
# i: 80  0.115846 ms
# i: 90  0.111374 ms
# i: 100  0.145382 ms

# Test 2: O(n)
# i: 10  0.000567 ms
# i: 20  0.00056  ms
# i: 30  0.000775 ms
# i: 40  0.000729 ms
# i: 50  0.000891 ms
# i: 60  0.001277 ms
# i: 70  0.001082 ms
# i: 80  0.001368 ms
# i: 90  0.001301 ms
# i: 100  0.001504 ms

# Test 3: O(n)
# i: 10  0.000347 ms
# i: 20  0.000367 ms
# i: 30  0.000391 ms
# i: 40  0.000403 ms
# i: 50  0.000405 ms
# i: 60  0.000761 ms
# i: 70  0.000439 ms
# i: 80  0.000443 ms
# i: 90  0.000445 ms
# i: 100  0.00047 ms

# Test 4: O(n^3)
# i: 10  0.046064 ms
# i: 20  0.238213 ms
# i: 30  0.587195 ms
# i: 40  1.191936 ms
# i: 50  2.153332 ms
# i: 60  3.596613 ms
# i: 70  5.538404 ms
# i: 80  7.954283 ms
# i: 90  11.364397 ms
# i: 100  15.135461 ms

# Test 5: O(n)
# i: 10  0.001247 ms
# i: 20  0.001548 ms
# i: 30  0.001803 ms
# i: 40  0.00541  ms
# i: 50  0.00243  ms
# i: 60  0.003038 ms
# i: 70  0.003127 ms
# i: 80  0.003605 ms
# i: 90  0.003974 ms
# i: 100  0.004019 ms
