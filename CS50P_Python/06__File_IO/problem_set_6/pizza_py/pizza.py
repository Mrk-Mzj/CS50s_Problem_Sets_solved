"""
https://cs50.harvard.edu/python/2022/psets/6/pizza/

In a file called pizza.py, implement a program that expects exactly one command-line argument, 
the name (or path) of a CSV file in Pinocchio’s format, 
and outputs a table formatted as ASCII art using tabulate, a package on PyPI at pypi.org/project/tabulate. 

Format the table using the library’s grid format. 

If the user does not specify exactly one command-line argument, or if the specified file’s name does not end in .csv, 
or if the specified file does not exist, the program should instead exit via sys.exit.
"""

import sys

path = "CS50P_Python/06__File_IO/problem_set_6/pizza_py/"

# file exception handling is another way to check if file exist,
# other than used in lines.py:  os.path.isfile(path + sys.argv[1])
try:
    with open(path + sys.argv[1], "r") as file:
        ...

except FileNotFoundError:
    sys.exit("you must add file name as a parameter")
