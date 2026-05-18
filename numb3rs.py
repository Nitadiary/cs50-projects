import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    pattern = r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$"
    match = re.search(pattern, ip)
    if not match:
        return False
    for group in match.groups():
        try:
            num = int(group)
        except ValueError:
            return False
        if num < 0 or num > 255:
            return False
        if str(num) != group:
            return False
    return True

if __name__ == "__main__":
    main()
