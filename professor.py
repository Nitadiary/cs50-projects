import random
def main():
    level = get_level()
    s = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        a = x + y

        attempts = 0
        while attempts < 3:
            try:
                g = int(input(f"{x} + {y} = "))
                if g == a:
                    s += 1
                    break
                else:
                    print("EEE")
                    attempts += 1
            except ValueError:
                print("EEE")
                attempts += 1
        if attempts >= 3:
            print(f"{x} + {y} =", a)

    print("score: ", s)

def get_level():
    while True:
        try:
            level = int(input("Enter your level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            continue

def generate_integer(level):

    if level not in [1, 2, 3]:
        raise ValueError("invalid")

    lower = 10**(level-1) if level > 1 else 0
    upper = (10**level) - 1
    return random.randint(lower, upper)



if __name__ == "__main__":
    main()
