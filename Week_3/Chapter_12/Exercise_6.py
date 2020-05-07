
def readposint():
    i = 0
    for _ in range(10):
        try:
            i = int(input("Please fill in a positive integer "))
            if i < 0:
               print("It is not a valid integer")
            elif i == 0:
                print("You have ended the proces")
                break
            print(i)
        except ValueError:
            print("You did not enter a positive integer, please fill in a positive integer")

    return i

if __name__ == "__main__":
    print(readposint())

