B = input("say greetings: ").lower().strip()

if B.startswith("hello"):
    print("$0")
elif B.startswith("h"):
    print("$20")
else:
    print("$100")

