name = input("What's your name? ")

# zapis:

# file = open("cs__06_02.txt", "w")
# file.write(f"{name}\n")
# file.close

# można skrócić i nie zapomni się o zamknięciu pliku:
with open("cs__06_02.txt", "a") as file:
    file.write(f"{name}\n")
