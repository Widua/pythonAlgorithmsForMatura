#Algorith does factorization

def factorize ( number ):
    print(number)
    prime = 2

    while number > 1:
        while number % prime == 0:
            number = int( number / prime )
            print( str(prime) + " " + str( number ) )
        prime+=1
    print("")
factorize( 12000 )
factorize( 560 )
factorize( 2137)