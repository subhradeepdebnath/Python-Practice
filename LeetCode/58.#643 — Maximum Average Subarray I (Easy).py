def func(arr,k):
    maxi=arr[0]
    for i in range(k):
        maxi=maxi+arr[i]
    total=maxi
    for i in range(k,len(arr)):
        total=total+arr[i]-arr[i-k]
        if total>maxi:
            maxi = total
    print(maxi/k)
arr=list(map(int, input().split()))
k=int(input())
func(arr,k)