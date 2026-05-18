def main():
    check_list = {}
    while True:
          try:
            item = input(" ").lower().strip()
            check_list[item] = check_list.get(item, 0) + 1
          except EOFError:
            for item in sorted(check_list.keys()):
                print(f"{check_list[item]} {item.upper()}")
            break

if __name__ == "__main__":
     main()
