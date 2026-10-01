def func(arr,ar):
    a=[]
    for i in range(m):
            a.append(arr[i])
    for i in range(n):
            a.append(ar[i])
    a.sort()
    print(*a)
arr=list(map(int, input().split()))
m=int(input())
ar=list(map(int, input().split()))
n=int(input())
func(arr,ar)