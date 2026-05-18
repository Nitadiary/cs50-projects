def emoji(e):
    #replacing emojies
    e = e.replace(":(","🙁")
    e = e.replace(":)","🙂")
    return e

def main():
    #asking for input
    i = input("Write your sentence here: ")
    s = emoji(i)
    print(s)

main()
