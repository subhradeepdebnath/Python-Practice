def func(arr):
    n=1
    while True:
        if n not in arr:
            print(n)
            return 
        n+=1
arr=list(map(int, input().split()))
func(arr)