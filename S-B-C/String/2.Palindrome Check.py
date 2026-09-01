s=input()
a=""
for i in range(len(s)-1,-1,-1):
    a=a+s[i]
if s==a:
    print("palindrome")
else:
    print("not palindrome")