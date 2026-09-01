def func(arr):
    freq={}
    for i in arr:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    maxi=max(freq)
    print(maxi)
arr=list(map(int, input().split()))
func(arr)