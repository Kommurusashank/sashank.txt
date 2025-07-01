a = [1, 3, 5, 6, 7, 2]
max1 = a[0]
for i in range(len(a)):
    if a[i] > max1:
        max1 = a[i]
second_max = a[0]
for i in range(len(a)):
    if a[i] != max1 and a[i] > second_max:
        second_max = a[i]
print(second_max)
