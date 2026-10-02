def func(arr):
    a=""
    for i in range(len(arr)-1,-1,-1):
        a=a+arr[i]+" "
    print(*a.strip(),sep="")
arr=input().split()
func(arr)