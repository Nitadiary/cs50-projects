def main():
  while True:
     try:
        a = input("please enter X/Y: ")
        x, y = a.split("/")
        x = int(x)
        y = int(y)

        f = (x/y)* 100
        f = round(f)

        if x > y or x/y < 0:
           raise ValueError

        if f <= 1:
            print("E")

        elif f >= 99:
            print("F")

        else:
            print(f"{f}%")

        break

     except (ValueError, ZeroDivisionError):
        print("Please enter the write number")

if __name__ == "__main__":
    main()
