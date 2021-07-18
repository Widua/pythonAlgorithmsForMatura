# Algorithm check is number perfect
import math


def isPerfect ( number ):
    sqrt = int( math.sqrt(number) )
    summedDividers = 1
    for i in range(2,int( sqrt )+1):

        if number % i == 0 :
            summedDividers += i + int(number/i)
    if number == sqrt * sqrt:
        summedDividers -= sqrt
    if summedDividers == number:
        return True
    else:
        return False

# Check perfect number
print(isPerfect(6))
print(isPerfect(28))
print(isPerfect(496))
print(isPerfect(8128))
print(isPerfect(33550336))
print(isPerfect(8589869056))
print(isPerfect(137438691328))

# Check non-perfect numbers

print(isPerfect( 2137 ))
print(isPerfect ( 420 ))
print(isPerfect( 6969 ))
print(isPerfect ( 29 ))