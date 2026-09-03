def func(arr, new):
    arr.append(new)
    arr.sort()
    result=[]
    result.append(arr[0])
    for i in range(1,len(arr)):
        if arr[i][0] <= result[-1][1]:
            result[-1][1]=max(result[-1][1],arr[i][1])
        else:
            result.append(arr[i])
    print(result)
n=int(input())
arr=[]
for i in range(n):
    data=list(map(int, input().split()))
    arr.append(data)
new=list(map(int, input().split()))
func(arr,new)