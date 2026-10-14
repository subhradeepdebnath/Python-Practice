def func(arr,target):
    i=0
    total=0
    mini = len(arr)+1
    for j in range(len(arr)):
        total=total+arr[j]
        while total>=target:
            length=j-i+1
            if length<mini:
                mini=length
            total=total-arr[i]
            i+=1
    if mini==len(arr)+1:
        print(0)
    else:
        print(mini)
arr=list(map(int, input().split()))
target=int(input())
func(arr,target)