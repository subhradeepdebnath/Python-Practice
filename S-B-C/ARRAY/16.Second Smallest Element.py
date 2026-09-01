arr=list(map(int,input().split()))
min=arr[0]
sec=arr[0]
for i in range(len(arr)):
    if arr[i]<min:
        min=arr[i]
for j in range(len(arr)):
    if arr[j]<sec and  arr[j]>min:
        sec=arr[j]
print(sec)