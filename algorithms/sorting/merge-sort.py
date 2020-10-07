"""
    Merge sort is created based on divide and conquer rule
    It takes less time than many other sorting algorithms
    Practically it takes about 0.22 seconds of time shorting about 20000 elements

    Average time complexity of merge sort is O(nlog n)

    In this code I have divide the main array into to sub arrays a,b
    then again merged a into two and b into two and again ... until the length of array becomes 1
    after the i have merged arrays reversely by sorting small arrays between them

    i have declared left and right. left means the left sub array after dividing the main array and right is right
        left -> a
        right -> b
"""


def merge(a, b):
    i, j, c = 0, 0, []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    if i == len(a):
        c.extend(b[j:])
    if j == len(b):
        c.extend(a[i:])
    return c


def mergeSort(array):
    if len(array) <= 1:
        return array
    left, right = mergeSort(array[:len(array) // 2]), mergeSort(array[len(array) // 2:])
    return merge(left, right)


print(mergeSort([10, 3, 18, 4, 32, 19, 27, 0, 3]))
