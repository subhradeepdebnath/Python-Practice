def func(arr):
    a=[]
    for i in range(len(arr)):
        if arr[i] in a:
            continue
        count=0
        for j in range(len(arr)):
            if arr[i]==arr[j]:
                count+=1
        print (arr[i],"->",count)
        a.append(arr[i])
arr=list(map(int, input().split()))
func(arr)