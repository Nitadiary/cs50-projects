k={"january" : 1,
"february" : 2,
"march" : 3,
"april" : 4,
"may" : 5,
"june" : 6,
"july" : 7,
"august": 8,
"september": 9,
"october": 10,
"november" : 11,
"december" : 12}

def main():
    y, m, d = date()
    print(f"{y:04d}-{m:02d}-{d:02d}")

def date():
    while True:
        i = input("Enter the date: ").strip()
        if "/" in i:
            try:
                a, b, c= map(int,i.split("/"))
                if c > 999 and 1 <= a <= 12 and 1 <= b <= 31:
                    y = c
                    d = b
                    m = a
                    return y, m, d
            except:
                pass
        elif "," in i:
            try:
                i = i.replace(",","").lower()
                i = i.split()
                if len(i) == 3:
                   month = i[0]
                   d = int(i[1])
                   y = int(i[2])
                   m = k.get(month)
                   if m and 1 <= d <= 31 and y > 0:
                       return y, m, d
            except:
                pass

if __name__ == "__main__":
    main()
