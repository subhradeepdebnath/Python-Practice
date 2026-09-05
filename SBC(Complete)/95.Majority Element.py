def func(arr):
    count={}
    n=len(arr)
    for i in arr:
        if i not in count:
            count[i]=1
        else:
            count[i]+=1
    for i in count:
        if count[i]>n//2:
            print(i)
            return
    print("No Majority")
arr=list(map(int,input().split()))
func(arr)