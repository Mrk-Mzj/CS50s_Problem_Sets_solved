# python cs_11_etc_03_argparse.py -n 3
# python cs_11_etc_03_argparse.py -n 3 -x 4
# python cs_11_etc_03_argparse.py -h

# Załóżmy, że piszemy program, który uruchamia się z parametrem "-n N"
# gdzie N to jakaś liczba. Łatwo napisać kilka linni do sczytywania wartości N.
# Problem pojawia się, gdy chcemy dać userowi możliwość wpisania od zera
# do kilku argumentów, w dowolnej kolejności. Tu przydaje się argparse.
# Dodatkowo obsłuży nam on komunikaty, jakie pojawią się po uruchomieniu programu
# z parametrem -h, czyli standardowym help.

import argparse

# Stworzenie obiektu, dodanie ogólnego opis działania programu:
parser = argparse.ArgumentParser(description="Meow like a cat")

# Zadeklarowanie obsługiwanych parametrów (-n), wpisanie wartości domyślnych,
# podpowiedzi helpa, oraz typu na jaki wartości mają być skonwertowane:
parser.add_argument("-n", default=1, help="number of times to meow", type=int)
parser.add_argument("-x", default=1, help="number of meows per line", type=int)

# Stworzenie obiektu reprezentującego wprowadzone parametry:
args = parser.parse_args()

for _ in range(args.n):
    print("meow!" * args.x)
