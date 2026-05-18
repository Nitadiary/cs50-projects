import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(H):
    pattern = r"^\s*(\d{1,2})(?::(\d{2}))?\s+(AM|PM)\s+to\s+(\d{1,2})(?::(\d{2}))?\s+(AM|PM)\s*$"

    H = re.search(pattern, H, re.IGNORECASE)
    if not H:
        raise ValueError

    h1, m1, ap1, h2, m2, ap2 = H.groups()
    m1 = m1 if m1 is not None else "00"
    m2 = m2 if m2 is not None else "00"

    try:
        int_h1 = int(h1)
        int_h2 = int(h2)
        int_m1 = int(m1)
        int_m2 = int(m2)
    except:
        raise ValueError

    if not (1 <= int_h1 <= 12):
        raise ValueError
    if not(1 <= int_h2 <= 12):
        raise ValueError
    if not (0 <= int_m1 <= 59):
        raise ValueError
    if not (0 <= int_m2 <= 59):
        raise ValueError

    h1_24h = hour24(int_h1, ap1.upper())
    h2_24h = hour24(int_h2, ap2.upper())

    return f"{h1_24h:02}:{int_m1:02} to {h2_24h:02}:{int_m2:02}"

def hour24(hour12:int, ampm:str):
    ampm = ampm.lower()
    if ampm == "am":
        return 0 if hour12 == 12 else hour12
    elif ampm == "pm":
        return 12 if hour12 == 12 else hour12 + 12
    else:
        raise ValueError

if __name__ == "__main__":
    main()
