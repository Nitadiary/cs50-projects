import sys
import os
from PIL import Image, ImageOps

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    i_file = sys.argv[1]
    o_file = sys.argv[2]

    valid_ending = [".jpg", ".jpeg", ".png"]
    i_ending = os.path.splitext(i_file)[1].lower()
    o_ending = os.path.splitext(o_file)[1].lower()

    if i_ending not in valid_ending or o_ending not in valid_ending:
        sys.exit("invalid input")

    if i_ending != o_ending:
        sys.exit("Input and output have different extensions")

    if not os.path.exists(i_file):
        sys.exit("can't find file")


    try:
        photo = Image.open(i_file)
        shirt = Image.open("shirt.png")
        size = shirt.size
        photo = ImageOps.fit(photo, size)
        photo.paste(shirt,(0, 0), shirt)
        photo.save(o_file)
    except FileNotFoundError:
        sys.exit("can't find file")

if __name__ == "__main__" :
    main()

