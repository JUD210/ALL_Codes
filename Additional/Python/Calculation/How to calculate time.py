""" 1 """
from time import time


def factorial1(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num


t0 = time()
factorial1(10 ** 5)
print("Elapsed time :", time() - t0)
# Elapsed time : 2.892544746398926

""" 2 """
import timeit


def factorial2(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num


t0 = timeit.default_timer()
factorial2(10 ** 5)
print("Elapsed time :", timeit.default_timer() - t0)
# Elapsed time : 3.3350997


""" 3 """
import cProfile


def factorial3(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num


cProfile.run("factorial3(10**5)")
#         4 function calls in 3.287 seconds

# Ordered by: standard name

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.000    0.000    3.287    3.287 <string>:1(<module>)
#     1    3.287    3.287    3.287    3.287 ___tempCodeRunnerFile.py:4(factorial3)
#     1    0.000    0.000    3.287    3.287 {built-in method builtins.exec}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}