# sprawdzenie czy input ma w sobie znak @

# usuwamy ew spacje przed lub po wpisanym mailu i dzielimy string na część przed i po @:
user_mail = input("\nWhat's your email?\n").strip()
username, domain = user_mail.split("@")


# jeśli istnieje część przed @, a część po @ zawiera kropkę...
if username and ("." in domain):
    print("\n> Good 1")
else:
    print("\n> Not good 1")


# trochę dokładniej:
if username and domain.endswith(".com"):
    print("> Good 2\n")
else:
    print("> Not good 2\n")
