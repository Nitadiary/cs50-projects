import emoji

def main():
    i = input("text: ")
    o = emoji.emojize(i, language = "alias")
    print(o)

if __name__ == "__main__":
    main()
