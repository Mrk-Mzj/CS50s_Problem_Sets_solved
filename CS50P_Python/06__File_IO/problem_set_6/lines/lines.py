"""
Implement a program that expects exactly one command-line argument, the name (or path) of a Python file, 
and outputs the number of lines of code in that file, excluding comments and blank lines. 

If the user does not specify exactly one command-line argument, 
or if the specified file’s name does not end in .py, or if the specified file does not exist, 
the program should instead exit via sys.exit.

Assume that any line that starts with #, optionally preceded by whitespace, is a comment. 
(A docstring should not be considered a comment.) Assume that any line that only contains whitespace is blank.
"""
# python CS50P_Python/06__File_IO/problem_set_6/lines/lines.py lines.py

import sys, os.path

path = "CS50P_Python/06__File_IO/problem_set_6/lines/"


# check if: file was run with 1 parameter, ending with .py, and pointing to a file that exists:
if (
    len(sys.argv) != 2
    or not sys.argv[1].endswith(".py")
    or not os.path.isfile(path + sys.argv[1])
):
    sys.exit("you must add file name as a parameter")


lines_of_code_count = 0

with open(path + sys.argv[1], "r") as file:
    print()

    for line in file:
        # ignore blank lines and comments; lstrip allows to ignore indented comments
        if line.isspace() or line.lstrip().startswith("#"):
            print(f"ignored: {line}", end="")
            pass
        else:
            lines_of_code_count += 1

print("\nLines of code:", lines_of_code_count)
