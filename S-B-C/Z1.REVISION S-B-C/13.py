def rev(s):
    a=""
    for ch in range(len(s)-1,-1,-1):
        a= a + s[ch]
    print(a)
s=input()
rev(s)