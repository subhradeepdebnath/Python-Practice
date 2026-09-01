#  given a list of numbers, check whether the list is sorted in ascending order or not?
arr = [1, 2, 3, 4, 5]
sorted=True
for i in range(len(arr)-1):
    if arr[i]>arr[i+1]:
        sorted=False
if sorted:
    print("sorted")
else:
    print("not sorted")