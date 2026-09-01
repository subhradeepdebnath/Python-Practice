arr=list(map(int, input().split()))
a=[]
for i in range(len(arr)):
    if arr[i] not in a:
        count=0
        for j in range(len(arr)):
            if arr[i]==arr[j]:
                count+=1
        if count>=2:
            print(arr[i],count)
        a.append(arr[i])