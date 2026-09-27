def func(s):
    new=s
    a=""
    for i in range(len(s)-1,-1,-1):
        a=a+s[i]
    if a==new:
        print("palindrome")
    else:
        print("not palindrome")
s=input()
func(s)