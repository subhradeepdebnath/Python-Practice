#  given  n numbers, find the smallest element in the list?
n=list(map(int,input().split()))
small=n[0]
for i in n:
    if i<small:
        small=i
print(small)