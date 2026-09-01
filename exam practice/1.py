

n=int(input())
initial=int(input())
ex=list(map(int, input().split()))
bonus=list(map(int, input().split()))
count=0
for i in range(n):
    if initial>=ex[i]:
        count+=1
        initial+=bonus[i]
print(count)
