def func(arr, target):
    minimum=len(arr)+1
    for i in range(len(arr)):
        sum=0
        for j in range(i,len(arr)):
            sum=sum+arr[j]
            if sum>=target:
                length=j-i+1
                if length<minimum:
                    minimum=length
    if minimum==len(arr)+1:
        print(0)
    else:
        print(minimum)
                
arr=list(map(int, input().split()))
target=int(input())
func(arr,target)