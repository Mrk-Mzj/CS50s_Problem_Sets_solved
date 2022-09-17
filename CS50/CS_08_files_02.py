name = input("What's your name? ")

# zapis:

# file = open("CS_08_files_01_text.txt", "w")
# file.write(f"{name}\n")
# file.close

# można skrócić i nie zapomni się o zamknięciu pliku:
with open("CS_08_files_01_text.txt", "w") as file:
    file.write(f"{name}\n")

