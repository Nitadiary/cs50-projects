import csv
import sys
import os
from tabulate import tabulate

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    f_name = sys.argv[1]
    if not f_name.lower().endswith(".csv"):
        sys.exit("not a csv file")
    if not os.path.exists(f_name):
        sys.exit("can't find file")
    try:
        with open(f_name, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            table = list(reader)

            print(tabulate(table, headers = "firstrow", tablefmt = "grid"))
    except FileNotFoundError:
        sys.exit("can't find file")
if __name__ == "__main__" :
    main()
