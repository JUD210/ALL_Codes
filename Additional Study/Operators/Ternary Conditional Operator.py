s = "Test String"

s1 = s if s is None else "Nothing"
s2 = s if s is not None else "Nothing"

print(s1, s2, sep="\n")
# Nothing
# Test String
