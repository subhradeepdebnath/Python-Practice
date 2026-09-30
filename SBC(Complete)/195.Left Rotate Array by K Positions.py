def func(arr, k ):
    n=len(arr)
    k=k% n 
    a=[]
    for i in range(k,n):
        a.append(arr[i])
    for i in range(k):
        a.append(arr[i])
    print(*a)
arr=list(map(int,input().split()))
k=int(input())
func(arr,k)