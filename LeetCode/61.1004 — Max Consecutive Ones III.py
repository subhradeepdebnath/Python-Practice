def func(arr,k):
    maxi=0
    for i in range(len(arr)):
        zero=0
        count=0
        for j in range(i,len(arr)):
            if arr[j]==0:
                zero+=1
            if zero>k:
                break
            count+=1
            if count<maxi:
                maxi=count
    print(maxi)