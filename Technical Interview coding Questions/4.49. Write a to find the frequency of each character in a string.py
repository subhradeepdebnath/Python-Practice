def func(arr):
    for i in range(len(arr)):
        count=0
        if arr[i] not in arr[:i]:
            for j in range(len(arr)):
                if arr[i]==arr[j]:
                    count+=1
            print(arr[i],"=",count)

arr=input()
func(arr)