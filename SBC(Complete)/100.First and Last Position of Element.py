def func(arr,target):
    a=[]
    for i in range(len(arr)):
            if arr[i]==target:
                a.append(i)
                break
    for i in range(len(arr)-1,-1,-1):
        if arr[i]==target:
            a.append(i)
            break
    print(*a)
arr=list(map(int, input().split()))
target=int(input())
func(arr,target)
