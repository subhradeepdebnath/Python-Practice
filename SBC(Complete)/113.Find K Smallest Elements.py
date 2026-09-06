def func(arr,k):
    arr.sort()
    a=[]
    for i in range(k):
        a.append(arr[i])
    print(*a)
arr=list(map(int, input().split()))
k=int(input())
func(arr,k)