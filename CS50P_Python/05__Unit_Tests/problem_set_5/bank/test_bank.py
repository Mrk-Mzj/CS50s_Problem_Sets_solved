# pip install -U pytest
# pytest test_bank.py


from bank import value


def test_value_zero():
    assert value("hello") == "0"
    assert value("Hello") == "0"
    assert value("HELLO") == "0"
    assert value("  HELLO  ") == "0"


def test_value_twenty():
    assert value("henlo") == "20"
    assert value("hhello") == "20"
    assert value("hello\\n") == "20"


def test_value_hundred():
    assert value(".hello") == "100"
    assert value("jo!") == "100"
    assert value("!^%$(ÓŁ") == "100"
    assert value("123") == "100"
    assert value("-123.456") == "100"
    assert value("") == "100"
