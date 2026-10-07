def func(n,arr):
    a=[]
    sum=0
    for i in range(len(arr)):
        sum+=arr[i]
        a.append(sum)
    print(min(a))
n=int(input())
arr=list(map(int, input().split()))
func(n,arr)