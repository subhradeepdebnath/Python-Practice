def func(arr,k):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i]==arr[j]:
                if j-i<=k:
                    print("true")
                    return
    print("false")
            
                
arr=list(map(int, input().split()))
k=int(input())
func(arr,k)