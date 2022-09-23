# sprawdzenie czy input ma w sobie znak @
# import modułu na potrzeby sprawdzenia #3
import re

# usuwamy ew spacje przed lub po wpisanym mailu i dzielimy string na część przed i po @:
user_mail = input("\nWhat's your email?\n").strip()
username, domain = user_mail.split("@")


# 1 jeśli istnieje część przed @, a część po @ zawiera kropkę...
if username and ("." in domain):
    print("\n> Good 1")
else:
    print("\n> Not good 1")


# 2 trochę dokładniej:
if username and domain.endswith(".com"):
    print("> Good 2")
else:
    print("> Not good 2")


# 3 z użyciem funkcji search z modułu re.search(r".+@.+\..+", user_mail)
# Pierwza część to pattern, druga to zmienna.

# .+  to co najmniej jeden znak,    @  to małpa,    .+  to co najmniej jeden znak,
# \.  to kropka,    .+  to co najmniej jeden znak

# Znak r na początku oznacza raw text. Używamy go na wszelki wypadek,
# by Python nie próbował interpretować backslasha jako znaku ucieczki,
# przedzielenia stringa. Gdyby nie "\." użycie r nie byłoby niezbędne.
# Ale warto r stosować, bo zwiększa niezawodność kodu przy modyfikacjach:

if re.search(r".+@.+\.com", user_mail):
    print("> Good 3")
else:
    print("> Not good 3")


# Powyższe sprawdzenie przepuści zdanie z kropką na końcu. Dodajmy znaki początku ^ i końca $.
# Przepuści też kilka znaków @. Dodajmy ograniczenia: [] -użyj tych znaków i [^] -nie używaj tych.
# ^[^@]+ oznacza "zacznij od co najmniej jednego znaku, poza @"
# [^@]+\.com$ to "skończ na co najmniej jednym znaku (poza @).com"

if re.search(r"^[^@]+@[^@]+\.com$", user_mail):
    print("> Good 4")
else:
    print("> Not good 4")


# Zamiast wykluczać @ i inne znaki specjalne, dopuśćmy wyłącznie wybrane znaki.
# Plus to nie sklejanie stringa; nadal oznacza "co najmniej 1 znak z przedziału"

if re.search(r"^[a-zA-Z0-9_.]+@[a-zA-Z0-9_.]+\.com$", user_mail):
    print("> Good 5")
else:
    print("> Not good 5")


# Możemy uprościć. Symbol \w oznacza dowolny znak alfanumeryczny lub podkreślnik.
# Dodaję kilka domen. Dodaję flagę, która pozwoli dopasować zarówno duże jak i małe litery.

if re.search(r"^[\w.]+@[\w.]+\.(com|com\.pl|pl)$", user_mail, re.IGNORECASE):
    print("> Good 6\n")
else:
    print("> Not good 6\n")

# Parametry można grupować w nawiasach, a nawiasy oznaczać jako występujące 0 lub 1 raz.
# Zapis \.(com\.)?pl$ obskoczy .com.pl i .pl

# Realnie regex dla poprawnego filtrowania adrersów email jest tak długi,
# że używa się do tego biblioteki.
