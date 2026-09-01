def func(arr,key):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j]==key:
                print(arr[i],arr[j])
                return
    else:
        print("no pair")
arr=list(map(int, input().split()))
key=int(input())
func(arr,key)