def func(arr):
    max=0
    for i in range(len(arr)):
        z=0
        o=0
        for j in range(i,len(arr)):
            if arr[j]==0:
                z+=1
            else:
                o+=1
            if z==o:
                length=j-i+1
                if length>max:
                    max=length
    print(max)
arr=list(map(int, input().split()))
func(arr)            
                