"""
https://cs50.harvard.edu/python/2022/psets/6/pizza/

In a file called pizza.py, implement a program that expects exactly one command-line argument, 
the name (or path) of a CSV file in Pinocchio’s Pizza format, 
and outputs a table formatted as ASCII art using tabulate, a package on PyPI at https://pypi.org/project/tabulate. 

Format the table using the library’s grid format. 

If the user does not specify exactly one command-line argument, or if the specified file’s name does not end in .csv, 
or if the specified file does not exist, the program should instead exit via sys.exit.
"""
# python CS50P_Python/06__File_IO/problem_set_6/pizza_py/pizza.py regular.csv


import sys
from tabulate import tabulate

PATH = "CS50P_Python/06__File_IO/problem_set_6/pizza_py/"
table = []


# check if there is one parameter, ending with .csv

if len(sys.argv) != 2 or not sys.argv[1].endswith(".csv"):
    sys.exit("you must add one CSV file name as a parameter")


# file exception handling is another way to check if file exist,
# other than used in lines.py:  os.path.isfile(...)
# although not as elegant.

try:
    with open(PATH + sys.argv[1], "r") as file:
        # copy CSV file into table of tables:

        for row in file:
            line = row.rstrip().split(",")
            table.append([line[0], line[1], line[2]])

    # print table using tabulate.
    # Make first row headers. Format in 'grid' style.

    print("\n" + tabulate(table, headers="firstrow", tablefmt="grid"))

except FileNotFoundError:
    sys.exit("file not found")
