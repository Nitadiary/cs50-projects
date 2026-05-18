import random

def main():
    while True:
        try:
            n = int(input("Determine the level: "))
            if n > 0:
                break
        except ValueError:
            pass
    s = random.randint(1,n)

    while True:
        try:
            g = int(input("Guess the number: "))
            if g <= 0:
                continue
        except ValueError:
            continue

        if g < s:
            print("Too small!")
        elif g > s:
            print("Too large!")
        else:
            print("Just right!")
            break

if __name__ == "__main__":
    main()
