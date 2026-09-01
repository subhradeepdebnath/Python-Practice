#  given an array , move all 0 s to the end while maintaining the order of the other elements.
n=int(input())
arr=list(map(int, input().split()))
new=[] 
for i in arr:
    if i != 0:
        new.append(i)
for i in arr:
    if i == 0:
        new.append(i)
print(new)