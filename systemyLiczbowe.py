# First algorith changes Number representation system.

def changeNumberRepresentationSystem(representation, number):
    if int(number > 0):
        changeNumberRepresentationSystem(representation, int(number / representation))
        if number % representation > 9:
            if number % representation == 10:
                print("A", end="")
            elif number % representation == 11:
                print("B", end="")
            elif number % representation == 12:
                print("C", end="")
            elif number % representation == 13:
                print("D", end="")
            elif number % representation == 14:
                print("E", end="")
            elif number % representation == 15:
                print("F", end="")
        else:
            print(number % representation, end="")

changeNumberRepresentationSystem(9, 5555)
