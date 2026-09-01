n=int(input())
arr=list(map(int, input().split()))
pos=0
neg=0
zero=0
for i in arr:
    if i>0:
        pos+=1
    if i<0:
        neg+=1
    if i==0:
        zero+=1
print(pos)
print(neg)
print(zero)
