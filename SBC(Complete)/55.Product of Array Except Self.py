def func(arr):
    result=[]
    for i in range(len(arr)):
        product=1
        for j in range(len(arr)):
            if i!=j:
                product=product*arr[j]
        result.append(product)
    print(*result)
arr=list(map(int, input().split()))
func(arr)