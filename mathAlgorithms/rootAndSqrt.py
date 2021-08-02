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

def sqrtWithDecimals( number ):
    precision = 0.00000000001
    a = 1
    b = number

    while abs( a - b ) >= precision:
        a = (a+b)/2
        b = number/a
    return a

number = root(3,3)
print(number)

number2 = sqrt(25)
print(number2)

number3 = sqrtWithDecimals( 111 )
print(number3)
