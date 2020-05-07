
def readposint():
    for _ in range(10):
        i = 0
        try:
            i = int(input("Please fill in a positive integer "))
            if i < 0:
                raise ValueError("(0) is not a valid integer",format(i))
            elif i == "x":
                print("You have ended the proces")
                break
            print(i)
        except ValueError:
            print("You did not enter a positive integer, please fill in a positive integer")


readposint()

