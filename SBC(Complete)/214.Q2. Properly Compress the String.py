def func(s):
    result=""
    for ch in "abcdefghijklmnopqrstuvwxyz":
        i=0
        total=0
        while i<len(s):
            if s[i]==ch:
                i+=1
                num=""
                while i<len(s) and s[i].isdigit():
                    num+=s[i]
                    i+=1
                total+=int(num)
            else:
                i+=1
        if total>0:
            result+=ch+str(total)
    print(result)
    
s=input()
func(s)