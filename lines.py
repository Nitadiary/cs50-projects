import sys
import os

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    filename = sys.argv[1]

    if not filename.endswith(".py"):
        sys.exit("Not a Python file")
    if not os.path.exists(filename):
        sys.exit("File does not exist")

    try:
        lines = count_lines(filename)
        print(lines)
    except FileNotFoundError:
        sys.exit("File does not exist")

def count_lines(filename):
    count = 0
    in_docstring = False
    with open(filename, "r", encoding ="utf-8") as f:
        for line in f:
            stripped = line.strip()
            if not stripped or stripped.startswith("#"):
                continue
            count += 1
    return count

if __name__ == "__main__":
    main()
