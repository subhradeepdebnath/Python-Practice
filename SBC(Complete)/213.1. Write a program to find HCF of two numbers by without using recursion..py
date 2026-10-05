def func(arr):
    arr.sort()
    hcf=0
    for i in range(1,arr[0]):
        if arr[0]%i==0 and arr[1]%i==0:
            if hcf<i:
                hcf=i
    print(hcf)
    
arr=list(map(int, input().split()))
func(arr)