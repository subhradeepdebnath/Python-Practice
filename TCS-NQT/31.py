#  given an array, print all elements that appear more than once?
n=int(input())
arr=list(map(int,input().split()))
for i in range(n):
    for j in range(i+1, n):
        if arr[i] == arr[j]:
            print(arr[i], end=" ")
            break
        