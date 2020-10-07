array = [9, -1, 0, 15, 5, 8, 19, 6, 3]
length = len(array)

for i in range(length - 1):
    min_ind = i
    for j in range(i + 1, length):
        if array[min_ind] > array[j]:
            min_ind = j

    x = array[i]
    array[i] = array[min_ind]
    array[min_ind] = x

print(array)
