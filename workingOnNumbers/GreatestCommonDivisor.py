#Algortihm give largest common diviser of two numbers, in two versions, first by subtraction larger number, second by using modulo (much more optimalized)

def gcd ( num1, num2 ):
    while num1 != num2:
        if num1 > num2:
            num1 -= num2
        else:
            num2 -= num1
    return num1


def ogcd ( num1, num2 ):

    while num2 != 0:
        help = num2
        num2 = num1 % num2
        num1 = help
    return num1

print(gcd( 28,24 ))
print(ogcd( 1,1000000 ))