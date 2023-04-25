# file = open("cs__06_02.txt", "a")
# file.write(f"{name}\n")
# file.close
# powyższy zapis można skrócić i nie zapomni się o zamknięciu pliku:

name = input("What's your name? ")

with open("cs__06_02.txt", "a") as file:
    file.write(f"{name}\n")
