def func(arr):
    arr=list(map(str,arr))
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i]+arr[j]<arr[j]+arr[i]:
                temp=arr[i]
                arr[i]=arr[j]
                arr[j]=temp
    if arr[0]=="0":
        print("0")
        return
    a=""
    for i in range(len(arr)):
        a=a+arr[i]
    print(a)    
arr=list(map(int, input().split()))
func(arr)