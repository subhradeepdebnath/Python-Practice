# arr=list(map(int, input().split()))
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         if arr[i]!= arr[j]:
#             print(arr[i])
#             break
#     else:
#         continue
#     break
arr=list(map(int, input().split()))
a=[] 
for i in range(len(arr)):
    if arr[i] not in a:
        count=0
        for j in range(len(arr)):
            if arr[i]==arr[j]:
                count+=1
        if count==1:
            a.append(arr[i])
            print(a[0])
            break