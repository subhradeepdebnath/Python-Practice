def rot(arr):
    a=[]
    num=arr[0]
    for i in range(1,len(arr)):
        a.append(arr[i])
    a.append(arr[0])
    print(a)
arr=list(map(int, input().split()))
rot(arr)