def func(arr):
    arr.sort()
    print(*arr,sep="->")
arr=list(map(int, input().split("->")))
func(arr)