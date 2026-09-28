def func(arr):
    p=0
    n=0
    z=0
    for i in range(len(arr)):
        if arr[i]>0:
            p+=1
        elif arr[i]<0:
            n+=1
        else:
            z+=1
    print(p)
    print(n)
    print(z)
arr=list(map(int, input().split()))
func(arr)