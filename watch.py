import sys
import re

def main():
    print(parse(input("HTML: ")))

def parse(s:str):
    L = re.search(r'<iframe[^>]*src="([^"]+)"',s)
    if not L:
        return None

    URL = L.group(1)
    pattern = r"^(https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+))$"
    A = re.search(pattern, URL)
    if not A:
        return None

    ID = A.group(2)
    return f"https://youtu.be/{ID}"

if __name__ == "__main__":
    main()
