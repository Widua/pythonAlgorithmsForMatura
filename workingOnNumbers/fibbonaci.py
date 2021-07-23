# Two algorithms, first write Fibonacci sequence, second return us sequence element

def fibbonaci ( howManyElements ):
    prevNumber = 0
    currentNumber = 1

    for i in range( howManyElements ):
        print(currentNumber)
        currentNumber +=prevNumber
        prevNumber = currentNumber - prevNumber

def fibbonaciRecurrent ( element ):

    if element < 3:
        return 1
    return fibbonaciRecurrent( element- 2 ) + fibbonaciRecurrent( element - 1 )


fibbonaci(10)
print("")
print(fibbonaciRecurrent( 10 ))