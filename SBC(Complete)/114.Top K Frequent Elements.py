def func(arr,k):
    a=[]
    v=[]
    for i in range(len(arr)):
        if arr[i] not in v:
            count=1
            for j in range(i+1,len(arr)):
                if arr[i]==arr[j]:
                    count+=1
            a.append([count,arr[i]])
            v.append(arr[i])
    a.sort(reverse=True)
    for i in range(k):
        print(a[i][1],end=" ")

arr=list(map(int,input().split()))
k=int(input())
func(arr,k)