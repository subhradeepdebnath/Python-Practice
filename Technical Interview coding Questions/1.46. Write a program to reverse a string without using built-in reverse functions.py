def func(arr):
    a=[]
    for i in range(len(arr)-1,-1,-1):
        a.append(arr[i])
        print(*a)
arr=input()
func(arr)