def func(arr):
    first=arr[0]
    ans=""
    for i in range(len(first)):
        for j in range(1,len(arr)):
            if i>=len(arr[j]) or first[i]!=arr[j][i]:
                print(ans)
                return
        ans=ans+first[i]
    print(ans)
arr= input().split()
func(arr)