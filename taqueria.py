def main():
    menu = {"baja taco": 4.00,
            "burrito": 7.50,
            "bowl": 8.50,
            "nachos": 11.00,
            "quesadilla": 8.50,
            "super burrito": 8.75,
            "super quesadilla": 9.50,
            "taco": 3.00,
            "tortilla salad": 8.00}

    total = 0.0

    try:
        while True:
            item =  input("Item: ").strip().lower()
            if item in menu:
                total += menu[item]
                print(f"Total price: ${total:.2f}")

    except EOFError:
        print("Order complete",f"${total:.2f}")
        return

if __name__ == "__main__":
    main()
