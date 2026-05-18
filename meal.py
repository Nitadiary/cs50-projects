def convert(T):
            H, M = T.split(":")
            H = float(H)
            M = float(M)
            T = H + M / 60
            return float(T)

def main():
    T = input("What time is it?(eg: 15:32) ")
    T = convert(T)

    if 7.00 <= T <= 8.00:
          print("Breakfast Time")

    elif 12.00 <= T <= 13.00:
          print("Lunch Time")

    elif 18.00 <= T <= 19.00:
          print("Dinner Time")

if __name__ == "__main__":
    main()
