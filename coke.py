def main():
     t = 50
     while t > 0:
          m = int(input(f"Amount Due:,{t},Insert your money (only 5, 10 and 25): "))
          if m in [5, 10, 25]:
               t -= m
               print("Amount Due:", t)
          else:
               print("Amount Due:", t)
     if t == 0:
          print("Change Owed: 0")
     elif t < 0:
          print("Change Owed:", -t)
     print("payment completed, you can take your drink!")
main()
