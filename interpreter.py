def main():
    N, Op, Z= input("Write your equasion here(eg: 3 + 6): ").strip().split()
    N = int(N)
    Z = int(Z)

    if Op == "+":
        result = N + Z
    elif Op == "-":
        result = N - Z
    elif Op == "*":
        result = N * Z
    elif Op == "/":
        result = N / Z
    else:
        print("invalid opration")
        return

    print(f"{result:.1f}")

main()
