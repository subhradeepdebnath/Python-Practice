def func(arr):
    total=0
    for i in range(len(arr)):
        sub=arr[i] - (i%7)*3
        if arr[i]%11==0:
            div=arr[i]/11
            total+=div+sub
        else:
            total+=sub
    print(total)
arr=list(map(int, input().split()))
func(arr)