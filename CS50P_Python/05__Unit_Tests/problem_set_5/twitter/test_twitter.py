# pip install -U pytest
# pytest test_twitter.py


from twitter import shorten


def test_numbers_shorten():

    assert shorten("123") == "123"
    assert shorten("15.2") == "15.2"
    assert shorten("0") == "0"
    assert shorten("-15.2") == "-15.2"
    assert shorten("-123") == "-123"


def test_specials_shorten():
    assert shorten("!@#%f\n") == "!@#%f\n"
    assert shorten(" ") == " "


def test_small_letters_shorten():
    assert shorten("abba") == "bb"
    assert shorten("ez gg") == "z gg"
    assert shorten("aeiouy") == ""


def test_large_letters_shorten():
    assert shorten("ABBA") == "BB"
    assert shorten("EZ GG") == "Z GG"
    assert shorten("AEIOUY") == ""
