"""
https://cs50.harvard.edu/python/2022/psets/6/scourgify/

In a file called scourgify.py, implement a program that:

1) Expects the user to provide two command-line arguments:
    - the name of an existing CSV file to read as input, 
      whose columns are assumed to be, in order: name and house;
    - the name of a new CSV to write as output, whose columns should be, in order: first, last, and house.

2) Converts that input to that output, splitting each name into a first name and last name. 
Assume that each student will have both a first name and last name.

If the user does not provide exactly two command-line arguments, or if the first cannot be read, 
the program should exit via sys.exit with an error message.
"""
# python CS50P_Python/06__File_IO/problem_set_6/scourgify/scourgify.py before.csv after.csv


import sys, os.path, csv

PATH = "CS50P_Python/06__File_IO/problem_set_6/scourgify/"
students = []


# check if user specified two arguments, and if the first one is readlible
if (
    len(sys.argv) != 3
    or not sys.argv[1].endswith(".csv")
    or not sys.argv[2].endswith(".csv")
    or not os.path.isfile(PATH + sys.argv[1])
):
    sys.exit(
        "\nYou must add valid input .csv file as the 1st parameter, and output .csv name as the 2nd"
    )


# reading file with csv.DictReader to clear quote marks
with open(PATH + sys.argv[1], "r") as file:
    reader = csv.DictReader(file)

    for line in reader:
        # creating table of tables,
        # splitting names in quotes, clearing spaces
        name = line["name"].split(",")
        students.append([name[1].strip(), name[0], line["house"]])


# TODO: saving "after.csv" file - best do in the same loop, as reading "before.csv"
print("\n", students)
