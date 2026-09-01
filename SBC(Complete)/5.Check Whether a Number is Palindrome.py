def func(n):
    rev=0
    num=n
    while n>0:
        digit=n%10
        rev=rev*10 +digit
        n=n//10
    if num==rev:
        print("palindrome number")
    else:
        print("not a palindrome number")
n=int(input())
func(n)