# Character Frequency Count
s=input()
v=[]
for i in s:
    if i not in v: 
        count=0
        for j in s:
            if i==j:
                count+=1
        print(i, count)
        v.append(i)