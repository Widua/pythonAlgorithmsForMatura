# Algorithm implements insertion sort

def insertionSort ( numbers ):
    for i in range ( 1 , len(numbers) ):
        helpVar = numbers[i]
        j = i - 1
        while j >= 0 and  numbers[j] > helpVar :
            numbers[j+1] = numbers [j]
            j-=1
        numbers[j+1] = helpVar
    return numbers

array = [55, 1, 99, 123, 9, 2137, 44, 555, 23, 2, 3, 6]
sortedArray = insertionSort( array )

for number in sortedArray :
    print(number, end=", ")