def pal(s):
    a=""
    for ch in range(len(s)-1,-1,-1):
        a=a+s[ch]
    if a==s:
        print("palidrome")
    else:
        print("not palindrome")
s=input()
pal(s)