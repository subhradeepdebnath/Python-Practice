def func(arr):
    maximum=0
    for i in range(len(arr)):
        zero=0
        one=0
        for j in range(i,len(arr)):
            if arr[j]==0:
                zero+=1
            else:
                one+=1
            if zero==one:
                length=j-i+1
                if length>maximum:
                    maximum=length
    print(maximum)
arr=list(map(int,input().split()))
func(arr)