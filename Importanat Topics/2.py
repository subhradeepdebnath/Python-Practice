#  Given an array arr containing n distinct numbers taken from the range 0 to n, find the only missing number.
arr=[3,0,1]
arr.sort()
missing=len(arr)
for i in range(len(arr)):
    if arr[i] != i:
        missing=i
        break
print(missing)