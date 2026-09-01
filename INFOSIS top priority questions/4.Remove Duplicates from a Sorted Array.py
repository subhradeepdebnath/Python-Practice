# Remove Duplicates from a Sorted Array

n=int(input())
arr=list(map(int, input().split()))
a=[]
for i in arr:
    if i not in a:
        a.append(i)
print(a)