def func(arr,val):
    m=len(arr)
    count=0
    a=[]
    for i in range(len(arr)):
        if arr[i]==val:
            count+=1
        else:
            a.append(arr[i])
    print("k=", m-count)
    print("nums=",a)
arr=list(map(int,input().split()))
val=int(input())
func(arr,val)