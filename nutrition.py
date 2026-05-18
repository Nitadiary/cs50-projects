def main():
    f = input("Write the fruits name: ").lower().strip()
    d = {"apple" : 130,
         "avocado" : 50,
         "sweet cherries" : 100,
         "banana": 110,
         "cantaloupe": 50,
         "grapefruit": 60,
         "grapes" : 90,
         "Honeydew melon": 50,
         "kiwifruit":90,
         "lemon":15,
         "lime":20,
         "nectarine":60,
         "orange":80,
         "peach":60,
         "pear":100,
         "pineapple":50,
         "plums":70,
         "strawberries":50,
         "tangerine": 50,
         "watermelon":80}
    if f in d:
        print("calories: ", d[f], "per every serving size")
    else:
        print("")
if __name__=="__main__":
    main()
