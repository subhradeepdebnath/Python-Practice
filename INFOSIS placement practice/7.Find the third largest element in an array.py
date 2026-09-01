n=int(input())
arr=list(map(int, input().split()))
first=float('-inf')
second=float('-inf')
third=float('-inf')
for i in arr:
    if i > first:
        third=second
        second= first
        first=i
    elif i>second and i!=first:
        third=second
        second=i
    elif i> third and i!=first and i!=second:
        third=i
print(third)