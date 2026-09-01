#  given an array, check whether it is sorted in ascending order or not?
n = int(input())
arr = list(map(int, input().split()))
sorted=True
for i in range(n-1):
    if (arr[i]>arr[i+1]):
        sorted=False
        break
if sorted:
    print("sorted")
else:
    print("not sorted")
    