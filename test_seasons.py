from seasons import calculate_m, ntow
import pytest
from datetime import date, timedelta

def test_one_year():
    today = date.today()
    one_year_ago = today - timedelta(days = 365)
    m = calculate_m(one_year_ago.strftime("%Y-%m-%d"))
    assert ntow(m) == "Five hundred twenty-five thousand, six hundred minutes"

def test_two_years():
    today = date.today()
    two_years_ago = today - timedelta(days = 730)
    m = calculate_m(two_years_ago.strftime("%Y-%m-%d"))
    assert ntow(m) == "One million, fifty-one thousand, two hundred minutes"

def test_five_years():
    today = date.today()
    five_years_ago = today - timedelta(days = 1826)
    m = calculate_m(five_years_ago.strftime("%Y-%m-%d"))
    assert ntow(m) == "Two million, six hundred twenty-nine thousand, four hundred forty minutes"

def test_invalid():
    with pytest.raises(ValueError):
        calculate_m("2020/12/01")
