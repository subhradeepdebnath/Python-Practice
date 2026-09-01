#  given a list of numbers, find whether the list contains any duplicate elements?
arr = [1, 2, 3, 4, 2]
found=False
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]==arr[j]:
            found=True
if found:
    print("duplicate found")
else:
    print("Duplicate not found")
        