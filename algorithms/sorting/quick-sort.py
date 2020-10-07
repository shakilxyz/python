def partition(array, low, high):
    i = low - 1
    pivot = array[high]

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1


def quickSort(array, low, high):
    if len(array) == 1:
        return array
    if low < high:
        pivot_index = partition(array, low, high)

        quickSort(array, low, pivot_index - 1)
        quickSort(array, pivot_index + 1, high)


array = [27, 39, 34, 2, 0, 47, 40, 27, 41, 14, 40, 49, 13, 13, 46, 20, 36, 27, 44, 15]
quickSort(array, 0, len(array)-1)

print(array)