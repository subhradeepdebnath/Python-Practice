# def fre(arr):
#     count=0
#     for i in range(len(arr)):
#         if arr[0]==arr[i]:
#             count+=1
#     return (arr[0],count)
# arr=list(map(int, input().split()))
# print(fre(arr))
def fre(arr):
    for i in range(len(arr)):
        count = 0
        for j in range(len(arr)):
            if arr[i] == arr[j]:
                count += 1
        print(arr[i], "->", count)
arr = list(map(int, input().split()))
fre(arr)