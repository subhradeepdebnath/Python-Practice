def func(arr,k):
    arr.sort()
    a=[]
    b=[]
    for i in range(len(arr)-1,-1,-1):
        a.append(arr[i])
    for i in range(k):
        b.append(a[i])
    print(b)
arr=list(map(int, input().split()))
k=int(input())
func(arr,k)