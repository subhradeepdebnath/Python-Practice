#  How many numbers are smaller than the current number?
n=int(input())
arr=list(map(int, input().split()))
new=[]
for i in arr:
    count=0
    for j in arr:
        if i>j:
            count+=1
    new.append(count)
print(new)