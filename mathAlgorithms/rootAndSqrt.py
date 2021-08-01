def root( number, power ):
    org = number
    for i in range(1,power):
        number = number * org
    return number

def sqrt(number):
    x = number
    y = 0

    while y**2 < x:
        y+=1
    return y

number = root(3,3)
number2 = sqrt(25)
print(number)
print(number2)