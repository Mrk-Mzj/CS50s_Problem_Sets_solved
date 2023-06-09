
Plik CSV ma zaletę w postaci łatwego przenoszenia między komputerami. To plik płaski, czyli odpowiednik pojedynczej tabeli w Excelu, bez dodatkowych arkuszy. Excel nie otworzy csv z milionem wpisów.

Wyciąganie i sprzątanie danych z CSV przy pomocy Pythona jest pracochłonne i powolne, zarówno na etapie pisania kodu, jak i czasu jego wykonywania. Przykład z wykładu:
https://cs50.harvard.edu/x/2022/notes/7/

SQL działa bardzo szybko. Pisanie w nim zajmuje wielokrotnie mniej czasu. Baza danych pozwala tworzyć wiele tabel i relacji między nimi.

</br>

## 1. Program SQLite

Działa w RAM, więc szybciej niż mySQL, ale nadaje się do mniejszych projektów. Można go obsługiwać z linii poleceń, lub wydawać komendy z kodu Pythona. 

SQLite3.exe używa się z terminalu i instaluje ze strony producenta: 
https://www.sqlite.org/download.html -> Precompiled Binaries for Windows -> sqlite-tools-win32-x86-....zip
Testy z wersji terminalowej SQLite wrzuciłem do osobnego folderu (07_02). Zaciągnąłem plik CSV, pozmieniałem zgodnie z wykładem, zapisałem do .DB poleceniem sqlite> .save favorites.db

</br>

## 2. Wtyczka 'SQLite' 
SQLite to również nazwa wtyczki do VSCode (autor: alexcvzz). 
Używa się przez wpisanie jej nazwy w okno [Ctrl + Shift + P] i wskazanie jej bazy danych do otwarcia. Pokaże tabele na dole exploratora. Da się sprawdzić wartość domyślną kolumny. Komendy dla tej wtyczki wpisuje się w pliku SQL. Więcej w folderze 07_01.

</br>

## 3. SQLite Viewer 
to inna, przydatna wtyczka. Pozwala wygodnie oglądać tablice wewnątrz pliku. Wystarczy kliknąć plik db. Wady? Nie pokaże wartości domyślnej, jaka może być przypisana do kolumny. Pokaże to .schema i pokaże to powyższa wtyczka #2.

</br>

## 4. Biblioteki
Python obsługuje pliki SQL dzięki bibliotekom. Najprostsza to CS50:

```bash
py -m pip install cs50
```
</br>

Komendy SQL: 

https://www.w3schools.com/sql/sql_select.asp
