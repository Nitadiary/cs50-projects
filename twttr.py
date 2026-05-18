t = input("Twit here: ")
v = ["A", "a", "E", "e", "I", "i", "U", "u", "O", "o"]
result = ""
for l in t:
    if l not in v:
        result += l
print(result)
