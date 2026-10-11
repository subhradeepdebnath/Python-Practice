def func(arr):
    a=[]
    for i in range(len(arr)):
        for j in range(len(arr)):
            for k in range(len(arr)):
                if arr[i]+arr[j]+arr[k]==0:
                    triplet=sorted([arr[i],arr[j],arr[k]])
                    if triplet not in a:
                        a.append(triplet)
    print(a)
arr=list(map(int, input().split()))
func(arr)