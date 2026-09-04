def func(s):
    rev=""
    for ch in range(len(s)-1,-1,-1):
        rev=rev+s[ch]
    print(rev)
s=input()
func(s)