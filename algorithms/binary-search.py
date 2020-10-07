"""
        Binary search takes very smaller amount of time which is about 0 seconds.
        It is the best efficient searching algorithm

        Note: the main problem of binary search is, before searching operation you must sort the list or array
            You can check my sorting algorithms. But in this code I have created a sorted list manually
"""

array = [0, 2, 13, 13, 14, 15, 20, 27, 27, 27, 34, 36, 39, 40, 40, 41, 44, 46, 47, 49]

n = int(input("Enter any number : "))
a, min_index, max_index = -1, 0, len(array)

while min_index != max_index:
    if array[(min_index + max_index) // 2] == n:
        print("{} found at index {}".format(n, (min_index + max_index) // 2))
        a = 1
        break
    elif array[(min_index + max_index) // 2] > n:
        max_index = (min_index + max_index) // 2
    elif array[(min_index + max_index) // 2] < n:
        min_index = (min_index + max_index) // 2 + 1

if a == -1:
    print("Element not in the list")
