def test_func():
    print("\n<<< in test_func >>>")
    while True:
        try:
            print("\n=== in try ===")
            int(input())
            return "end in try"
        except ValueError:
            print("=== in ValueError exception ===")
            break            
            return "end in ValueError"
            # The finally block is run before the method returns

        finally:
            print("=== in finally ===")
            return "end in finally"

        return "end in while"
    return "end out of while"