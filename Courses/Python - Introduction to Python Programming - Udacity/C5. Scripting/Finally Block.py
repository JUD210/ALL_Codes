while True:
    try:
        print("\n=== in try ===")
        int(input())
        break
    except ValueError:
        print("=== in ValueError exception ===")

    finally:
        print("=== in finally ===")
# === in try ===
# Nope
# === in ValueError exception ===
# === in finally ===
#
# === in try ===
# 5
# === in finally ===


def test_func():
    print("\n<<< in test_func >>>")
    while True:
        try:
            print("\n=== in try ===")
            int(input())
            return "end in try"
        except ValueError:
            print("=== in ValueError exception ===")
            return "end in ValueError"  # or break
            # The finally block is run before return, break.

        finally:
            print("=== in finally ===")
            return "end in finally"
            # Also notice that even though the program crashes, codes in the finally block will be still executed.

        return "end in while"
    return "end out of while"


print(test_func())
# <<< in test_func >>>
#
# === in try ===
# 5
# === in finally ===
# end in finally


# <<< in test_func >>>
#
# === in try ===
# Nope
# === in ValueError exception ===
# === in finally ===
# end in finally


