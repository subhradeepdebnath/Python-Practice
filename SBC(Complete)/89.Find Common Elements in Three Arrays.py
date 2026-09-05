def func(a1,a2,a3):
    a=[]
    for i in range(len(a1)):
        if a1[i] in a2 and a1[i] in a3:
            a.append(a1[i])
    for i in range(len(a2)):
            if a2[i] in a1 and a2[i] in a3 and a2[i] not in a: 
                a.append(a2[i])
    for i in range(len(a3)):
            if a3[i] in a2 and a3[i] in a1 and a3[i] not in a:
                a.append(a3[i])
    print(*a)
a1=list(map(int, input().split()))
a2=list(map(int, input().split()))
a3=list(map(int, input().split()))
func(a1,a2,a3)
