def func(arr):
    for i in range(len(arr)):
        count=0
        for j in range(len(arr)):
            if arr[i]==arr[j]:
                count+=1
        if count==2:
            print("true")
            return
    else:
        print("false")
arr=list(map(int, input().split()))
func(arr)