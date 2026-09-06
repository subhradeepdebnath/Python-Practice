def func(arr,k):
    a=[]
    arr.sort()
    for i in range(len(arr)-1,-1,-1):
        a.append(arr[i])
    for i in range(len(a)):
        print(a[k-1])
        return
arr=list(map(int, input().split()))
k=int(input())
func(arr,k)