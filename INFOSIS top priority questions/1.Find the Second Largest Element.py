# Find the Second Largest Element
n=int(input())
arr=list(map(int, input().split()))
first=float('-inf')
second=float('-inf')
for i in arr:
    if i>first:
        second=first
        first=i
    elif i>second and i!=first:
        second=i
if second==float('-inf'):
    print(-1)
else:
    print(second)
