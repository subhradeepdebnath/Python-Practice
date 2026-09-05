def func(arr,k):
    maximum=0
    for i in range(len(arr)-k+1):
        sum=0
        for j in range(i, i+k):
            sum=sum+arr[j]
        if i==0 or sum>maximum:
            maximum=sum
    print(maximum)
arr=list(map(int, input().split()))
k= int (input())
func(arr,k)