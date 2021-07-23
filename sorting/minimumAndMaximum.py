# This algorithm select minimum and maximum number in array

def findMin ( numbers ):
    currentLowest = numbers[0]
    for number in numbers:
        if number < currentLowest:
            currentLowest = number
    return currentLowest

def findMax ( numbers ):
    currentHighest = numbers[0]
    for number in numbers:
        if number > currentHighest:
            currentHighest = number
    return currentHighest


def findMinAndMax ( numbers ):
    tabMin = []
    tabMax = []
    for i in range(0,len(numbers)-1, 2):
        if numbers[i] > numbers[i+1]:
            tabMin.append( numbers[i+1] )
            tabMax.append( numbers [i] )
        else:
            tabMin.append(numbers[i])
            tabMax.append(numbers[i+1])

    min = findMin( tabMin )
    max = findMax( tabMax )
    print( "Minimum: "+ str( min ) )
    print( "Maximum: "+ str( max ) )





array = [ 1, 10,50, -50, 90, 2136 ,85, 128, 255, 1024, 314 ]

findMinAndMax(array)