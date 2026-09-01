n=int(input())
arr=list(map(int, input().split()))
key=int(input())
a=[]
for i in arr:
    if i>key:
        a.append(i)
print(*a)