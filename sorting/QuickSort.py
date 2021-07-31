# Quick sort algorithm
# Great thanks to Rob Edwards, with his help on youtube video : https://youtu.be/ZHVk2blR45Q I understood how work quick sort algorithm

def quickSort( numbers, leftIndex, rightIndex ):
    if leftIndex < rightIndex:
        # Initialization
        # i - border between numbers smaller than pivot, and greater than pivot

        i = leftIndex
        pivotIndex = int( (leftIndex+rightIndex) /2 )
        pivot = numbers[pivotIndex]

        # Swapping pivot with last element, just for simpler loop
        numbers[rightIndex] , numbers[pivotIndex] = numbers[pivotIndex] , numbers[rightIndex]

        # Loop that iterates numbers from left to right, and setting our border
        for j in range( leftIndex, rightIndex ):
            if numbers[j] < pivot:
                numbers[i], numbers[j] = numbers[j], numbers[i]
                i+=1
        # swapping pivot to good placer with smaller numbers on left, and greater numbers on right
        numbers[rightIndex], numbers[i] = numbers[i], numbers[rightIndex]

        # recurrent invokes of function to left and right side of pivot
        quickSort(numbers, leftIndex, i )
        quickSort(numbers,i+1, rightIndex)


array = [55, 1, 99, 123, 9, 2137, 44, 555, 23, 2, 3, 6]
quickSort(array, 0, len(array) - 1)
print(array)
