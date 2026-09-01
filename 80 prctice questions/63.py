#  given a list of numbers, find the second largest number without using sort() and min()?
arr = [8, 3, 1, 6,10,88, 2]
largest=arr[0]
second=arr[0]
for i in arr:
    if i>largest:
        largest=i
for i in arr:
    if i>second and i<largest:
        second=i
print(second)