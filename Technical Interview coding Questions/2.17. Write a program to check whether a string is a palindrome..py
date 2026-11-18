def func(arr):
    a=""
    for i in range(len(arr)-1,-1,-1):
        a=a+arr[i]
    if arr==a:
        print("palindrome")
    else:
        print("not palindrome")
arr=input()
func(arr)