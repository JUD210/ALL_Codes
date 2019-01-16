""" Quiz: Check for Prime Numbers

Prime numbers are whole numbers that have only two factors: 1 and the number itself. The first few prime numbers are 2, 3, 5, 7.

For instance, 6 has four factors: 1, 2, 3, 6.
1 X 6 = 6
2 X 3 = 6
So we know 6 is not a prime number.

In the following coding environment, write code to check if the numbers provided in the list check_prime are prime numbers.

- If the numbers are prime, the code should print "[number] is a prime number."
- If the number is NOT a prime number, it should print "[number] is not a prime number", and a factor of that number, other than 1 and the number itself: "[factor] is a factor of [number]".


Example output:

7 is a prime number
26 is not a prime number
2 is a factor of 26 
"""


## Your code should check if each number in the list is a prime number
check_prime = [26, 39, 51, 53, 57, 79, 85]

## write your code here
## HINT: You can use the modulo operator to find a factor

for num in check_prime:
    factor = []

    for n in range(1, num + 1):
        if num % n == 0:
            factor.append(n)

    if len(factor) == 2:
        result = "a prime number"
    else:
        result = "not a prime number"

    print("{} is {}".format(num, result))
    print("{}'s factors: {}".format(num, factor))
    print("")

