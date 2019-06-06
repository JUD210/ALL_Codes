import os, sys, inspect

# realpath() will make your script run, even if you symlink it :)
cmd_folder = os.path.realpath(
    os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe()))[0])
)

if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)

##### Above is not from this course.

camelot_path = cmd_folder + "/Sub Files/camelot.txt"

"""
Conveniently, Python will loop over the lines of a file using the syntax for line in file. I can use this to create a list of lines in the file. Because each line still has its newline character attached, I remove this using .strip().
"""

camelot_lines = []
with open(camelot_path) as f:
    for line in f:
        camelot_lines.append(line)

print(camelot_lines)
# ["We're the knights of the round table\n", "We dance whenever we're able"]


camelot_lines = []
with open(camelot_path) as f:
    for line in f:
        camelot_lines.append(line.strip())

print(camelot_lines)
# ["We're the knights of the round table", "We dance whenever we're able"]
