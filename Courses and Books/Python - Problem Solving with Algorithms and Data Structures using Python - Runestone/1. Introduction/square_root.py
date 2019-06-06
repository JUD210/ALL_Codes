def sqrt(n):
    """ 
    Using Newton's Method
    """

    root = n/2    #initial guess will be 1/2 of n
    for _ in range(20):
        root = (1/2)*(root + (n / root))

    return root


print(sqrt(9))
# 3.0
print(sqrt(4563))
# 67.54998149518622
