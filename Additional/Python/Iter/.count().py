txt = """
ABCDEF
ABCDEF
"""
print(txt)
# 
# ABCDEF
# ABCDEF
# 

print(txt.count("\n"))
# 3


l = [s for s in txt]
print(l)
# ['\n', 'A', 'B', 'C', 'D', 'E', 'F', '\n', 'A', 'B', 'C', 'D', 'E', 'F', '\n']

print(l.count("\n"))
# 3
