import inflect

n = inflect.engine()
names = []

while True:
    try:
        name = input(" ")
        names.append(name)
    except EOFError:
        break

B = n.join(names)
print(f"Adieu, adieu, to {B}")
