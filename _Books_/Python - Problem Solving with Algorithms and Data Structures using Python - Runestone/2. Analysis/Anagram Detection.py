# https://runestone.academy/runestone/static/pythonds/AlgorithmAnalysis/AnAnagramDetectionExample.html


import itertools
import time

start = time.time()


def anagram_solution1(s1, s2):
    """ Solution 1. Checking Off : O(n^2)

    T(n)
    = n + n-1 + n-2 + ... 2 + 1
    = {n(n+1)}/2
    = 1/2 n^2 + 1/2 n

    """
    start = time.time()

    if len(s1) != len(s2):
        return False, time.time() - start

    for pos1 in range(len(s1)):

        found: bool
        for pos2 in range(len(s2)):
            if s1[pos1] == s2[pos2]:
                found = True

        if not found:
            print(time.time() - start)
            return False, time.time() - start

    return True, time.time() - start


def anagram_solution2(s1, s2):
    """ Solution 2. Sort and Compare : (maybe) O(n logn)

    Sorting is typically either O(n2) or O(n logn), so the sorting operations 'dominate' the iteration.
    In the time.time(), this algorithm will have the same order of magnitude as that of the sorting process.

    """
    start = time.time()

    if len(s1) != len(s2):
        return False, time.time() - start

    lst1 = sorted(list(s1))
    lst2 = sorted(list(s2))

    for pos in range(len(lst1)):
        if lst1[pos] != lst2[pos]:

            return False, time.time() - start

    return True, time.time() - start


def anagram_solution3(s1, s2):
    """ Solution 3: Brute Force : O(n!)

    When generating all possible strings from s1, there are n possible first characters, n-1 possible characters for the second position, n-2 for the third, and so on.

    n * (n-1) * (n-2) *  ...  * 3 * 2 * 1 , which is n!

    """
    start = time.time()

    if len(s1) != len(s2):
        return False, time.time() - start

    tpl = tuple(s2)

    for subset in itertools.permutations(s1, len(s1)):
        if subset == tpl:
            return True, time.time() - start
    return False, time.time() - start


def anagram_solution4(s1, s2):
    """ Solution 4. Count and Compare : O(n)

    T(n) = 2n+26

    But, this algorithm sacrificed space in order to gain time.


    """
    start = time.time()

    c1 = [0] * 26
    c2 = [0] * 26

    for i in range(len(s1)):
        pos = ord(s1[i]) - ord("a")
        c1[pos] = c1[pos] + 1

    for i in range(len(s2)):
        pos = ord(s2[i]) - ord("a")
        c2[pos] = c2[pos] + 1

    for j in range(26):
        if c1[j] == c2[j]:
            continue
        else:
            return False, time.time() - start

    return True, time.time() - start


result = []

start = time.time()
tmp = anagram_solution1("abcdjefghi" * 1000, "ihgfejdcba" * 1000)
print(f"Result1 is {tmp[0]}\t | required {tmp[1]:.20f} seconds")

result.append(["anagram_solution1: O(n^2)", time.time() - start])
print(result[0])
print("")


start = time.time()
tmp = anagram_solution2("abcdjefghi" * 1000, "ihgfejdcba" * 1000)
print(f"Result2 is {tmp[0]}\t | required {tmp[1]:.20f} seconds")

result.append(["anagram_solution2: (maybe) O(n logn)", time.time() - start])
print(result[1])
print("")


# start = time.time()
# tmp = anagram_solution3("abcdjefghi * 1000", "ihgfejdcba" * 1000)
print(f"Result3 is (gonna be True)\t | FREEZE because it's O(n!)")
print("")

start = time.time()
tmp = anagram_solution4("abcdjefghi" * 1000, "ihgfejdcba" * 1000)
print(f"Result4 is {tmp[0]}\t | required {tmp[1]:.20f} seconds")

result.append(["anagram_solution4: O(n)", time.time() - start])
print(result[2])
print("")

tmp2 = sorted(result, key=lambda result: result[1])
print("=== Efficiency ===")
print(
    "\n".join(f"{str(l[0]).ljust(40)}\t Average : {(l[1]):.5f} sec" for l in tmp2)
)  # type: ignore


# Result1 is True	 | required 8.96987009048461914062 seconds
# ['anagram_solution1: O(n^2)', 8.96987009048462]

# Result2 is True	 | required 0.00300025939941406250 seconds
# ['anagram_solution2: (maybe) O(n logn)', 0.0030002593994140625]

# Result3 is (gonna be True)	 | FREEZE because it's O(n!)

# Result4 is True	 | required 0.00800275802612304688 seconds
# ['anagram_solution4: O(n)', 0.008002758026123047]

# === Efficiency ===
# anagram_solution2: (maybe) O(n logn)    	 Average : 0.00300 sec
# anagram_solution4: O(n)                 	 Average : 0.00800 sec
# anagram_solution1: O(n^2)               	 Average : 8.96987 sec
