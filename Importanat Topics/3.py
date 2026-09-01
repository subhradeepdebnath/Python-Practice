# #  Given an integer array arr of size n where:
# Every number is in the range 1 to n.
# Some numbers appear twice.
# Some numbers are missing.
# Return all the numbers that are missing.

n=int(input())
arr=list(map(int, input().split()))
new=[]
d=[]
for i in range(1, n+1):
    new.append(i)
    if i not in arr:
        d.append(i)
print(d)