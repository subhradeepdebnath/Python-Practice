def func(arr):
    max=0
    element=0
    for i in range(len(arr)):
        count=0
        for j in range(len(arr)):
            if arr[i] == arr[j]:
                count+=1
        if count>max:
            max=count
            element=arr[i]
    print(element)
        
arr=list(map(int, input().split()))
func(arr)