a = int(input("enter your lucky number: "))

# match (a) like this if complicated case!

match a:
    case 1:
        print("you won pizza")
    case 3:
        print("won camera")
    case 9:
        print("won biryani")
    case _:
        print("better luck next time")
#case _: default
