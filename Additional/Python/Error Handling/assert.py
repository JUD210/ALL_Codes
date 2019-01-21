for c in "abcABC":
    try:
        assert c.islower()
    except:
        print(f"{c} is not lower case.")
    else:
        print(f"{c} is lower case.")
    finally:
        print("===")
# a is lower case.
# ===
# b is lower case.
# ===
# c is lower case.
# ===
# A is not lower case.
# ===
# B is not lower case.
# ===
# C is not lower case.
# ===