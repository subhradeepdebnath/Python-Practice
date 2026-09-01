# First Non-Repeating Character
s=input()
for i in s:
    count=0
    for j in s:
        if i == j:
            count+=1
    if count==1:
        print(i)
        break
else:
    print(-1)