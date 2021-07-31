# Algorithm implements Merge Sort

def mergeSort ( numbers ):
    length = len( numbers )

    if length > 1:
        mid = int(length /2)
        leftArray = numbers[:mid]
        rightArray = numbers[mid:]
        # split array
        mergeSort(leftArray)
        mergeSort(rightArray)

        # Merge algorithm
        leftSize = len(leftArray)
        rightSize = len( rightArray )

        i = 0 # i - Left index
        j = 0 # j - Right index
        m = 0 # m - main array index

        while i < leftSize and j < rightSize:
            if leftArray[i] < rightArray[j]:
                numbers[m] = leftArray[i]
                i += 1
            else:
                numbers[m] = rightArray[j]
                j += 1
            m+=1

        # If arrays are not eqal, this lines put missing numbers in array
        while i < leftSize :
            numbers[m] = leftArray[i]
            i+=1
            m+=1
        while j < rightSize :
            numbers[m] = rightArray[j]
            j+=1
            m+=1


array = [55, 1, 99, 123, 9, 2137, 44, 555, 23, 2, 3, 6]
mergeSort(array)
print(array)