"""
    Linear search is a simple and basic searching algorithm
    Just construct a for loop which iterate over the array and
        matches every elements of the loop with the desired number.
    The loop will iterate until the number is found or it reaches at the end of the array

    This should not be use in codes because it takes lot of time iterating a large list.
    Even your program can crash
"""

array = [4, 2, 19, 10, 6, 3, 67, 41, 18, 95]

n = int(input("Enter an integer : "))
switch = False
for i in range(len(array)):
    if n == array[i]:
        print("Found {} at position {}".format(n, i))
        switch = True
        break

if not switch:
    print("Not found")