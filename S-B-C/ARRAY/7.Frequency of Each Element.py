# arr=list(map(int, input().split()))
# a=[]
# for i in range(len(arr)):
#     if arr[i] not in a:
#         count=0
#         for j in range(len(arr)):
#             if arr[i]==arr[j]:
#                 count+=1
#         a.append(arr[i])
#         print(arr[i],count)


arr=list(map(int, input().split()))
freq={}
for i in range(len(arr)):
    if arr[i] in freq:
        freq[arr[i]]=freq[arr[i]]+1
    else:
        freq[arr[i]]=1
for key in freq:
    print(key, freq[key])