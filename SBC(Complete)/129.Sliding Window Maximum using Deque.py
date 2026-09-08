def func(arr,k):
    a=[]
    for i in range(len(arr)-k+1):
        maximum=arr[i]
        for j in range(i,i+k):
            if arr[j]>maximum:
                maximum=arr[j]
        a.append(maximum)
    print(*a)

arr=list(map(int,input().split()))
k=int(input())
func(arr,k)