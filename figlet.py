from pyfiglet import Figlet
import sys
import random

def main():
    figlet = Figlet()
    fonts = figlet.getFonts()

    if len(sys.argv) == 1:
        f = random.choice(fonts)

    elif len(sys.argv) == 3:
        op = sys.argv[1]
        f_name = sys.argv[2]

        if op not in ["-f", "--font"]:
            sys.exit("invalid")

        elif f_name not in fonts:
            sys.exit("invalid")
        f = f_name

    else:
        sys.exit("error")

    figlet.setFont(font=f)
    t = input("write your text: ")
    print(figlet.renderText(t))

if __name__ == "__main__":
    main()
