arr=list(map(int, input().split()))
a=[]
max=0
ele=arr[0]
for i in range(len(arr)):
    if arr[i] not in a:
        count=0
        for j in range(len(arr)):
            if arr[i]==arr[j]:
                count+=1
        a.append(arr[i])
        if count > max:
            max=count
            ele=arr[i]
print(ele)