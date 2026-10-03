def func(arr):
    arr.sort()
    lenn=1
    maxx=1
    for i in range(1,len(arr)):
        if arr[i]==arr[i-1]+1:
            lenn+=1
        else:
            lenn=1
        if lenn>maxx:
            maxx=lenn
    print(maxx)
arr=list(map(int,input().split()))
func(arr)