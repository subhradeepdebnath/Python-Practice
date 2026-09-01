#  given an array, rotate it to the right by 1 position?
n=int(input())
arr= list(map(int, input().split()))
last=arr[n-1]
for i in range(n-1, 0, -1):
    arr[i] = arr[i-1]
arr[0]=last
print(arr)
