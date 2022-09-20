# sklejanie 2 plików PNG w animowany GIF

# instalowanie biblioteki Pillow: 
# python3 -m pip install --upgrade pip
# python3 -m pip install --upgrade Pillow

"""
python cs_08_files_11_GIF.py cs_08_files_11_1.png cs_08_files_11_2.png
"""

import sys
from PIL import Image

animacja = []

# dla wszystkich argumentów, poza nazwą programu, wykonaj

for arg in sys.argv[1:]:
    klatka = Image.open(arg)
    animacja.append(klatka)

# zapisz pierwszą klatkę animacji do pliku GIF,
# z uwzględnieniem wszystkich przekazanych jej klatek,
# z przekazaniem jej klatki [1]
# a wynikowy plik ma wyświetlać klatkę przez 200 ms, nieskończoną ilość razy

animacja[0].save(
    "cs_08_files_11_animacja.gif",
    save_all=True,
    append_images=[animacja[1]],
    duration=500,
    loop=0,
)

# gotowego GIFa można otworzyć bezpośrednio w VSCode