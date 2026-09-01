n=int(input())
m=int(input())
count=0
for i in range(1,n+1):
    for j in range(1,n+1):
        if j%i==0:
            print([i,j])
            count+=1
print(count)