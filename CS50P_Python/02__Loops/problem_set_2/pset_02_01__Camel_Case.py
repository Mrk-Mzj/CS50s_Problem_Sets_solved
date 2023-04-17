"""
ask for camelCaseNamedVariable
convert it to snake_case_named_variable
"""

snake_case_name = ""
camelCaseName = input("camelCaseName: ")


for letter in camelCaseName:
    if letter == letter.upper():
        letter = "_" + letter.lower()
    snake_case_name += letter


print(snake_case_name)

# snake_case_name = ...
# print(snake_case_name)
