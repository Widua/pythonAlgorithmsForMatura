#Second algorith check that number is prime

def isPrime ( number ):
    for i in range(2,int(number/2)):
        if number % i :
            return False
    return True
print( isPrime(5) )
print( isPrime(8) )