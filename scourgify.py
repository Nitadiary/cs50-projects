import sys
import csv

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    i_file = sys.argv[1]
    o_file = sys.argv[2]


    try:
        with open(i_file, "r", encoding = "utf-8") as infile:
            reader = csv.DictReader(infile)
            with open(o_file, "w",newline = "", encoding = "utf-8") as outfile:
                f_names = ["first", "last", "house"]
                writer = csv.DictWriter(outfile, fieldnames = f_names)
                writer.writeheader()

                for row in reader:
                    last, first = row["name"].split(", ")
                    house = row["house"]
                    writer.writerow({ "first": first, "last": last, "house": house})
    except FileNotFoundError:
        sys.exit(f"couldnt read {i_file}")

if __name__ == "__main__" :
    main()
