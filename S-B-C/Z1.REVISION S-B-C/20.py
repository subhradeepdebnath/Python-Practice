def func(arr,key):
    for i in range(len(arr)):
        if arr[i]==key:
            print(True)
            break
    else:
        print(False)
arr=list(map(int, input().split()))
key=int(input())
func(arr,key)