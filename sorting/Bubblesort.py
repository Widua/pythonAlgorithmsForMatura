# This algorithm implement Bubblesort

def bubbleSort ( numbers ):
    for i in range(0,len(numbers)):
        for a in range(1,len(numbers)-i):
            if numbers[a - 1] > numbers[a]:

                numbers[a-1],numbers[a] = numbers[a] , numbers[a-1]

    return numbers


array = [ 55, 1, 99, 123, 9, 2137, 44, 555, 23, 2, 3, 6 ]

sortedArray = bubbleSort( array )

for number in sortedArray:
    print( number , end=", " )