def func(arr):
    freq={}
    for x in arr:
        if x in freq:
            freq[x]+=1
        else:
            freq[x]=1
    print(freq)
arr=list(map(int, input().split()))
func(arr)