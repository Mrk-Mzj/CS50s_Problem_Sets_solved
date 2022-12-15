# pip install -U pytest
# pytest test_Vanity_Plates.py

# “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
# “No periods, spaces, or punctuation marks are allowed.”
# “All vanity plates must start with at least two letters.”

# “Numbers cannot be used in the middle of a plate; they must come at the end.
# For example, AAA222 would be an acceptable vanity plate; AAA22A would not be acceptable.
# The first number used cannot be a ‘0’.”


from Vanity_Plates import is_valid


def test_is_valid_length():
    assert is_valid("") == False
    assert is_valid("a") == False
    assert is_valid("aa") == True
    assert is_valid("aaaaaa") == True
    assert is_valid("aaaaaaa") == False


def test_is_valid_special_chars():
    assert is_valid("  ") == False
    assert is_valid("..") == False
    assert is_valid(",,") == False
    assert is_valid("\n\n") == False
    assert is_valid("  aa") == False
    assert is_valid("..aa") == False
    assert is_valid(",,aa") == False
    assert is_valid("\n\naa") == False


def test_is_valid_starts_with_2_letters():
    assert is_valid("aa") == True
    assert is_valid("aa5") == True
    assert is_valid("a5") == False
    assert is_valid("5a") == False
    assert is_valid("55") == False


def test_is_valid_numbers_at_end():
    assert is_valid("aa5") == True
    assert is_valid("aaa5") == True
    assert is_valid("aa5a") == False
    assert is_valid("aa5a5") == False


def test_is_valid_zero():
    assert is_valid("aa50") == True
    assert is_valid("aa05") == False
