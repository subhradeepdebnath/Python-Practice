#  given n numbers, find the largest element in the list?
n=list(map(int,input().split()))
large=n[0]
for i in n:
    if i>large:
        large=i
print(large)