def func(arr):
    visited=[]
    for i in range(len(arr)):
        if arr[i] not in visited:
            count=0
            for j in range(len(arr)):
                if arr[i]==arr[j]:
                    count+=1
            if count==1:
                print(arr[i])
                return
            visited.append(arr[i])
        

arr=list(map(int, input().split()))
func(arr)
