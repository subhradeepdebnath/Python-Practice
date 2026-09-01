#  Sort a list in ascending order( without using sort())
arr=list(map(int,input().split()))
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]> arr[j]:
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
print(arr)