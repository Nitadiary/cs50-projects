def main():
    plate = input("write your plate number: ").upper()

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(plate:str):
    if not (2 <= len(plate) <= 6):
        return False
    if not isinstance(plate, str):
        return False
    if not plate.isalnum():
        return False
    if not plate[0].isalpha() or not plate[1].isalpha():
        return False

    digit_started = False

    for char in plate:
        if char.isdigit():

            if not digit_started:
                digit_started = True
                if char == '0':
                     return False
                else:
                     continue
        elif digit_started:
                return False
    return True

if __name__ == "__main__":
    main()
