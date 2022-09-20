name = input("What's your name? ")

# zapis:

# file = open("CS_08_files_02.txt", "w")
# file.write(f"{name}\n")
# file.close

# można skrócić i nie zapomni się o zamknięciu pliku:
with open("cs_08_files_02.txt", "a") as file:
    file.write(f"{name}\n")
