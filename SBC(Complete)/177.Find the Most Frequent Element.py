def func(arr):
    cout=0
    max=arr[0]
    for i in range(len(arr)):
        count=0
        for j in range(len(arr)):
            if arr[i]==arr[j]:
                count+=1
        if count>cout:
            cout=count
            max=arr[i]
    print(cout,max)
arr=list(map(int, input().split()))
func(arr)