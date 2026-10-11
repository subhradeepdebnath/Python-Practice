def func(arr):
    arr=arr.lower()
    a=""
    for i in range(len(arr)):
        if arr[i].isalnum():
            a=a+arr[i]
    if a==a[::-1]:
        print("palindrome")
    else:
        print("not palindrome")
arr=input()
func(arr)