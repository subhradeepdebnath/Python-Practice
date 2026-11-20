def func (arr):
    a=""
    for i in range(len(arr)):
        if arr[i] not in a:
            a=a+arr[i]
    print(*a,sep="")
arr=input()
func(arr)