n=int(input())
arr=list(map(int, input().split()))
first=float('-inf')
second=float('-inf')
for i in arr:
    if i > first:
        first=i
    if i>second and i!=first:
        second=i
print(second)