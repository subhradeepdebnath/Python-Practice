def func(arr):
    s=[]
    for i in arr:
        s.append(i)
    print(s)
    x=s.pop(0)
    print(x)
    print(s)
arr=list(map(int, input().split()))
func(arr)