# https://docs.google.com/spreadsheets/d/1TOqKK0oJQX-jKGsH8lx69bg7nQdfE_t0BTpKprIo3Bc/edit#gid=36601067


# |    Operation     | Big-O Efficiency |
# | ---------------- | ---------------- |
# | index []         | O(1)             |
# | index assignment | O(1)             |
# | append           | O(1)             |
# | pop()            | O(1)             |
# | pop(i)           | O(n)             |
# | insert(i,item)   | O(n)             |
# | del operator     | O(n)             |
# | iteration        | O(n)             |
# | contains (in)    | O(n)             |
# | get slice [x:y]  | O(k)             |
# | del slice        | O(n)             |
# | set slice        | O(n+k)           |
# | reverse          | O(n)             |
# | concatenate      | O(k)             |
# | sort             | O(n log n)       |
# | multiply         | O(nk)            |


import timeit


def test1():
    lst = []
    for i in range(1000):
        lst = lst + [i]
    return lst


def test2():
    lst = []
    for i in range(1000):
        lst.append(i)
    return lst


def test3():
    lst = [i for i in range(1000)]
    return lst


def test4():
    lst = list(range(1000))
    return lst


t1 = timeit.Timer("test1()", "from __main__ import test1")
print("concat ", t1.timeit(number=1000), "milliseconds")
t2 = timeit.Timer("test2()", "from __main__ import test2")
print("append ", t2.timeit(number=1000), "milliseconds")
t3 = timeit.Timer("test3()", "from __main__ import test3")
print("comprehension ", t3.timeit(number=1000), "milliseconds")
t4 = timeit.Timer("test4()", "from __main__ import test4")
print("list range ", t4.timeit(number=1000), "milliseconds")
# concat  1.4311097 milliseconds
# append  0.08616500000000005 milliseconds
# comprehension  0.046829599999999916 milliseconds
# list range  0.0288520000000001 milliseconds


popzero = timeit.Timer("x.pop(0)", "from __main__ import x")
popend = timeit.Timer("x.pop()", "from __main__ import x")
for i in range(1_000_000, 10_000_001, 1_000_000):
    x = list(range(i))
    pe = popend.timeit(number=1000)
    x = list(range(i))
    pz = popzero.timeit(number=1000)
    print(f"i:{i}\npop(0): {pz} milliseconds\npop( ): {pe} milliseconds\n")
# i:1000000
# pop(0): 1.1131841999999998 milliseconds
# pop( ): 7.929999999989334e-05 milliseconds
#
# i:2000000
# pop(0): 2.2524481 milliseconds
# pop( ): 7.570000000001187e-05 milliseconds
#
# i:3000000
# pop(0): 3.3524668999999996 milliseconds
# pop( ): 7.29000000001534e-05 milliseconds
#
# i:4000000
# pop(0): 4.6747779000000005 milliseconds
# pop( ): 7.300000000043383e-05 milliseconds
#
# i:5000000
# pop(0): 5.696958799999999 milliseconds
# pop( ): 7.62999999999181e-05 milliseconds
#
# i:6000000
# pop(0): 6.846045099999998 milliseconds
# pop( ): 7.769999999851507e-05 milliseconds
#
# i:7000000
# pop(0): 7.923427399999998 milliseconds
# pop( ): 9.790000000009513e-05 milliseconds
#
# i:8000000
# pop(0): 8.963241199999999 milliseconds
# pop( ): 0.00011139999999443262 milliseconds
#
# i:9000000
# pop(0): 10.139602699999998 milliseconds
# pop( ): 7.919999999472793e-05 milliseconds
#
# i:10000000
# pop(0): 11.344610700000004 milliseconds
# pop( ): 8.090000000038344e-05 milliseconds
