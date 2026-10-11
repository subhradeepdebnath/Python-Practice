def func(arr,k):
    a=[]
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            for k in range(j+1,len(arr)):
                for l in range(k+1,len(arr)):
                    if arr[i]+arr[j]+arr[k]+arr[l]==k:
                        triplet=sorted([arr[i],arr[j],arr[k],arr[l]])
                        if triplet not in a:
                            a.append(triplet)
    print(a)
arr=list(map(int, input().split()))
k=int(input())
func(arr,k)