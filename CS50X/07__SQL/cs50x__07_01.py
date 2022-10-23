# Plik CSV ma zaletę w postaci łatwego przenoszenia między komputerami.
# To plik płaski, czyli odpowiednik pojedynczej tabeli w Excelu, bez dodatkowych arkuszy.
# Excel nie otworzy csv z milionem wpisów.
#
# Wyciąganie i sprzątanie danych z CSV przy pomocy Pythona jest pracochłonne i powolne,
# zarówno na etapie pisania kodu, jak i czasu jego wykonywania. Przykład z wykładu:
# https://cs50.harvard.edu/x/2022/notes/7/
#
# SQL działa bardzo szybko. Pisanie w nim zajmuje wielokrotnie mniej czasu. Baza danych
# pozwala tworzyć wiele tabel i relacji między nimi.
#
# Użyjemy programu SQLite.
# Działa w RAM, więc szybciej niż mySQL, ale nadaje się do mniejszych projektów.
# Można go obsługiwać z linii poleceń, lub wydawać komendy z kodu Pythona.
# Instaluje się go jako wtyczkę do VSCode (autor: alexcvzz),
# albo ze strony producenta https://www.sqlite.org/download.html -> Precompiled Binaries
# for Windows -> sqlite-tools-win32-x86-....zip

# Python obsługuje pliki SQL dzięki bibliotekom. Najprostsza to CS50:
# py -m pip install cs50
#
