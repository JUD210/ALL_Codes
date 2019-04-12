# https://runestone.academy/runestone/static/pythonds/AlgorithmAnalysis/WhatIsAlgorithmAnalysis.html


import time

# I can simplify many codes using timeit module.
# But I wouldn't do that because it's time wasting.


def sum_of_n_stupid(n):
    start = time.time()

    the_sum = 0
    for i in range(1, n + 1):
        the_sum = the_sum + i

    end = time.time()

    return the_sum, end - start


def sum_of_n_clever(n):
    start = time.time()

    the_sum = (n * (n + 1)) / 2
    end = time.time()

    return the_sum, end - start


result = []

start = time.time()
for _ in range(5):
    print("Sum is %d\t|  required %.20f seconds" % sum_of_n_stupid(1_000_000))

result.append(["Sum_of_n_stupid 1", (time.time() - start) / 5])
print(result[0])
print("")


start = time.time()
for _ in range(5):
    print(
        f"Sum is {sum_of_n_stupid(1000000)[0]}\t|  required {sum_of_n_stupid(1000000)[1]:.20f} seconds"
    )

result.append(["Sum_of_n_stupid 2", (time.time() - start) / 5])
print(result[1])
print("")


start = time.time()
for _ in range(5):
    tmp = sum_of_n_stupid(1_000_000)
    print(f"Sum is {tmp[0]}\t|  required {tmp[1]:.20f} seconds")

result.append(["Sum_of_n_stupid 3", (time.time() - start) / 5])
print(result[2])
print("")


start = time.time()
for _ in range(5):
    tmp = sum_of_n_clever(1_000_000)
    print(f"Sum is {tmp[0]}\t|  required {tmp[1]:.20f} seconds")

result.append(["Sum_of_n_clever", (time.time() - start) / 5])
print(result[3])
print("")


tmp2 = sorted(result, key=lambda result: result[1])
print("=== Efficiency ===")
print("\n".join(f"{l[0]}\t Average : {(l[1]):.5f} sec" for l in tmp2))  # type: ignore

# Sum is 500000500000	|  required 0.05701375007629394531 seconds
# Sum is 500000500000	|  required 0.05501246452331542969 seconds
# Sum is 500000500000	|  required 0.05601263046264648438 seconds
# Sum is 500000500000	|  required 0.06101298332214355469 seconds
# Sum is 500000500000	|  required 0.06101369857788085938 seconds
# ['Sum_of_n_stupid 1', 0.05821313858032227]

# Sum is 500000500000	|  required 0.04701066017150878906 seconds
# Sum is 500000500000	|  required 0.05501246452331542969 seconds
# Sum is 500000500000	|  required 0.04601025581359863281 seconds
# Sum is 500000500000	|  required 0.04701042175292968750 seconds
# Sum is 500000500000	|  required 0.04901051521301269531 seconds
# ['Sum_of_n_stupid 2', 0.10061893463134766]

# Sum is 500000500000	|  required 0.05201196670532226562 seconds
# Sum is 500000500000	|  required 0.04901146888732910156 seconds
# Sum is 500000500000	|  required 0.04901051521301269531 seconds
# Sum is 500000500000	|  required 0.04801082611083984375 seconds
# Sum is 500000500000	|  required 0.05001020431518554688 seconds
# ['Sum_of_n_stupid 3', 0.050011301040649415]

# Sum is 500000500000.0	|  required 0.00000000000000000000 seconds
# Sum is 500000500000.0	|  required 0.00000000000000000000 seconds
# Sum is 500000500000.0	|  required 0.00000000000000000000 seconds
# Sum is 500000500000.0	|  required 0.00000000000000000000 seconds
# Sum is 500000500000.0	|  required 0.00000000000000000000 seconds
# ['Sum_of_n_clever', 0.0]

# === Efficiency ===
# Sum_of_n_clever	 Average : 0.00000 sec
# Sum_of_n_stupid 3	 Average : 0.05001 sec
# Sum_of_n_stupid 1	 Average : 0.05821 sec
# Sum_of_n_stupid 2	 Average : 0.10062 sec
