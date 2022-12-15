# return text with all wovels omitted (A, E, I, O, and U).


def main():

    long_text = input("input your text: ")    
    print(shorten(long_text))


def shorten(long_text):

    HARAM = ["A", "E", "I", "O", "U", "Y"]
    shrt_txt = ""

    for _ in long_text:
        if _.upper() not in HARAM:
            shrt_txt += _
    return shrt_txt


if __name__ == "__main__":
    main()
