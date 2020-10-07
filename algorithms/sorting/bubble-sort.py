a = [9, -1, 0, 15, 5, 8, 19, 6, 3]

for p in range(0, len(a)):
    for q in range(p + 1, len(a)):
        if a[p] > a[q]:
            a[p], a[q] = a[q], a[p]

print(a)