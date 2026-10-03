def func(arr,ar):
    a=[]
    for i in range(len(arr)):
        if arr[i] in ar and arr[i] not in a:
            a.append(arr[i])
    for i in range(len(ar)):
            if ar[i] in arr and ar[i] not in a:
                a.append(ar[i])  
    print(*a)   
arr=list(map(int, input().split()))
ar=list(map(int, input().split()))
func(arr,ar)