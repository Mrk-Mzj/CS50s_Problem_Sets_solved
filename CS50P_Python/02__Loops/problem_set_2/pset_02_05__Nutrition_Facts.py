"""
implement a program that prompts consumers users to input a fruit (case-insensitively)
and then outputs the number of calories in one portion of that fruit.
Capitalization aside, assume that users will input fruits exactly as written in the poster (e.g., strawberries, not strawberry).
Ignore any input that isn’t a fruit.
"""


fruits = {"apple": 130, "banana": 110, "grape": 90, "lemon": 15, "orange": 80}
fruit = input("Which fruit? (apple, banana, grape, lemon, orange)\n")

if fruit in fruits:
    print(fruits[fruit], "kcal")
