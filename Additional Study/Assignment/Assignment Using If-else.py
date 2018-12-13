_input = "Test String"

string1 = _input if _input is None else "Nothing"
string2 = _input if _input is not None else "Nothing"

print(string1, string2, sep="\n")
# Nothing
# Test String
