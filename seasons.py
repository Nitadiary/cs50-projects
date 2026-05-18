from datetime import date, datetime
import sys
import inflect
import math

def main():
    try:
        b_date = input("enter your Birth date: ")
        m = calculate_m(b_date)
        print(ntow(m))
    except ValueError:
        sys.exit("invalid date")

def calculate_m(b_date):
    try:
        BD = datetime.strptime(b_date, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("invalid")

    today = date.today()
    delta = today - BD
    days = delta.days
    m = days*24*60
    return m

def ntow(m):
    p = inflect.engine()
    w = p.number_to_words(m, andword="")
    return w.capitalize() + " minutes"

if __name__ == "__main__":
    main()
