def func(arr):
    a=arr[0]
    b=[]
    for i in range( 1,len(arr)):
        b.append(arr[i])
    print(*(b+[a]))
arr=list(map(int, input().split()))
func(arr)