# return text with all wovels omitted (A, E, I, O, and U).

long_text = input("input your text: ")
shrt_txt = ""
haram = ["A", "E", "I", "O", "U", "Y"]


for _ in long_text:
    if _.upper() not in haram:
        shrt_txt += _


print(shrt_txt)
