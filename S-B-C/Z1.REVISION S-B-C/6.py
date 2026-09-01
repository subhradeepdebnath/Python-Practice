def search(arr,key):
    for i in range(len(arr)):
        if (arr[i])==key:
            return i
arr=list(map(int, input().split()))
key=int(input())
print(search(arr,key))