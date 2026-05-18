i = input("Write camelCase name here: ")
j = ""

for c in i:
    if c.isupper():
        j += "_" + c.lower()
    else:
        j += c

print(j)
