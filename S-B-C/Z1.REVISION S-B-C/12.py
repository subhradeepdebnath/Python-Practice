def vow(s):
    count=0
    for ch in s:
        if ch in "AEIOUaeiou":
            count+=1
    print(count)
s=input()
vow(s)