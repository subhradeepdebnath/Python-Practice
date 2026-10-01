def func(arr):
    a=[]
    for i in range(len(arr)):
        mul=1
        for j in range(len(arr)):
            if i!=j:
                mul*=arr[j]
        a.append(mul)
    print(a,sep=",")
arr=list(map(int, input().split()))
func(arr)