def func(arr):
    mini=arr[0]
    profit=0
    for i in range(1,len(arr)):
        if arr[i]<mini:
            mini=arr[i]
        else:
            current_profit=arr[i]- mini
            if current_profit>profit:
                profit=current_profit
    print(profit)
arr=list(map(int, input().split()))
func(arr)