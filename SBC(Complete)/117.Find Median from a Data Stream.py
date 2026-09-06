def func(arr):
    a=[]
    for i in range(len(arr)):
        a.append(arr[i])
        a.sort()
        n=len(a)
        if n%2==1:
            print(a[n//2])
        else:
            mid1=a[n//2-1]
            mid2=a[n//2]
            print((mid1+mid2)/2)
arr=list(map(int, input().split()))
func(arr)