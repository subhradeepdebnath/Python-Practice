def func(s):
    count=0
    cout=0
    cou=0
    for ch in s:
        if ch in "aeiouAEIOU":
            count+=1
        elif ch ==" ":
            cout+=1
        elif ch.isalpha():
            cou+=1
    print(count)
    print(cout)
    print(cou)
s=input()
func(s)