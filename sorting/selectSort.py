# Algorithm implements selection sort

def selectionSort( numbers ):
    for i in range (0, len( numbers ) ):

        for a in range( i+1 , len(numbers) ):
            if numbers[i] > numbers[a]:
                helpVar = numbers[i]
                numbers[i] = numbers[a]
                numbers[a] = helpVar
    return numbers


array = [55, 1, 99, 123, 9, 2137, 44, 555, 23, 2, 3, 6]

sortedArray = selectionSort( array )

for number in sortedArray:
    print( number , end=", " )