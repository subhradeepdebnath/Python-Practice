def func(arr):
    for i in range(len(arr)):
        count=0
        for j in range(len(arr)):
            if arr[i]==arr[j]:
                count+=1
        if count==1:
            print(i)
            return
    print(-1)
arr=input()
func(arr)