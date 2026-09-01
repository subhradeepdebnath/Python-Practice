# Merge Two Sorted Arrays
n=int(input())
arr1=list(map(int, input().split()))
m=int(input())
arr2=list(map(int, input().split()))
a=[]
for i in arr1:
        a.append(i)
for i in arr2:
        a.append(i)
a.sort()
print(*a)