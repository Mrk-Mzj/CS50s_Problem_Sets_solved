# pytest CS50P_Python/08__Object_Oriented_Programming/problem_set_8/Seasons_of_Love/test_seasons.py

from seasons import convert_str_to_date_object
import pytest


def test_positive():
    # test for positive outcome

    assert str(convert_str_to_date_object("2000-12-12")) == "2000-12-12"
    assert str(convert_str_to_date_object("0001-01-01")) == "0001-01-01"


def test_negative(capfd):
    # test for system exit with error message

    # testing for literal birth date
    with pytest.raises(SystemExit) as e:
        convert_str_to_date_object("December twelfth, nineteen ninety-nine")
    out, err = capfd.readouterr()
    assert e.type == SystemExit
    assert str(e.value) == "\nError: invalid birth date"

    # testing for birth date greater than today
    with pytest.raises(SystemExit) as e:
        convert_str_to_date_object("2222-12-31")
    out, err = capfd.readouterr()
    assert e.type == SystemExit
    assert str(e.value) == "\nError: invalid birth date"
