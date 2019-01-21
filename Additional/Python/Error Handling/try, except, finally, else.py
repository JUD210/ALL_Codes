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


##############################


def test_func():
    print("\n<<< in test_func >>>")
    while True:
        try:
            print("\n=== in try ===")
            int(input())

            print("=== end of try ===")

        except ValueError:
            print("=== in ValueError exception ===")

            print("=== end of ValueError Exception ===")

            return "end in ValueError Exception"  # or break
            # The finally block is run before return, break.

        else:
            print("=== in else ===")

            print("=== end of else ===")

        finally:
            print("=== in finally ===")
            # Also notice that even though the program crashes, codes in the finally block will be still executed.

            print("=== end of finally ===")

        return "end in while"
    return "end out of while"


print(test_func())
# <<< in test_func >>>
#
# === in try ===
# 5
# === end of try ===
# === in else ===
# === end of else ===
# === in finally ===
# === end of finally ===
# end in while


# <<< in test_func >>>
#
# === in try ===
# nope
# === in ValueError exception ===
# === end of ValueError Exception ===
# === in finally ===
# === end of finally ===
# end in ValueError Exception
