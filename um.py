import sys
import re

def main():
    print(count(input("write your text: ")))

def count(s: str)->int:
    um_find = re.findall(r"\bum\b", s, re.IGNORECASE)
    return len(um_find)

if __name__ == "__main__":
    main()
