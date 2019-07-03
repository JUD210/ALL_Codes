import os, sys, inspect

# realpath() will make your script run, even if you symlink it :)
cmd_folder = os.path.realpath(
    os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe()))[0])
)

if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)

##### Above is not from this course.

test_hello_path = cmd_folder + "/Sub Files/test_hello.txt"


""" Reading a File

1. First open the file using the built-in function, open. This requires a string that shows the path to the file. The open function returns a file object, which is a Python object through which Python interacts with the file itself. Here, we assign this object to the variable f.

2. There are optional parameters you can specify in the open function. One is the mode in which we open the file. Here, we use r or read only. This is actually the default value for the mode argument.

3. Use the read method to access the contents from the file object. This read method takes the text contained in a file and puts it into a string. Here, we assign the string returned from this method into the variable file_data.

4. When finished with the file, use the close method to free up any system resources taken up by the file.
"""

f = open(test_hello_path)
# f = open(test_hello_path, "r")
file_data = f.read()
f.close()


""" Writing to a File

1. Open the file in writing ('w') mode. If the file does not exist, Python will create it for you. If you open an existing file in writing mode, any content that it had contained previously will be deleted. If you're interested in adding to an existing file, without deleting its content, you should use the append ('a') mode instead of write.

2. Use the write method to add text to the file.

3. Close the file when finished.

"""

f = open(test_hello_path, "w")
f.write("Hello there!\nGood to See you.")
f.close()


""" Too Many Open Files

Run the following script in Python to see what happens when you open too many files without closing them!
"""

# files = []
# for i in range(10000):
#     files.append(open(test_hello_path, "r"))
#     print(i)

# OSError: [Errno 24] Too many open files: 'd:\\Google Drive\\ALL CODES\\CS Study Note\\[Python] Introduction to Python Programming (Udacity)\\C5. Scripting/Sub Files/test_hello.txt'


""" With

This with keyword allows you to open a file, do operations on it, and automatically close it after the indented code is executed, in this case, reading from the file.

Now, we don't have to call f.close()! You can only access the file object, f, within this indented block.
"""

with open(test_hello_path) as f:
    file_data = f.read()
# f = open('another_file.txt', 'r')
# file_data = f.read()
# f.close()

print(file_data)
# Hello there!
# Good to See you.

""" Calling the read Method with an Integer """

with open(test_hello_path) as f:
    file_data = f.read(2), f.read(8), f.read()
print("\n".join(file_data))
# He
# llo ther
# e!
# Good to See you.

""" Reading Line by Line """

with open(test_hello_path) as f:
    file_data = f.readline(), f.readline(), f.readline()
print(*file_data)
# Hello there!
#  Good to See you.
