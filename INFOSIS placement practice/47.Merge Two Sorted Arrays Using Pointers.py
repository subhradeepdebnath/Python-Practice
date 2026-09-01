# Merge Two Sorted Arrays Using Pointers
n1=int(input())
arr1=list(map(int,input().split()))
n2=int(input())
arr2=list(map(int,input().split()))

i=0
j=0
c=[]

while i<n1 and j<n2:
    if arr1[i] < arr2[j]:
        c.append(arr1[i])
        i+=1
    else:
        c.append(arr2[j])
        j+=1

while i<n1:
    c.append(arr1[i])
    i+=1

while j<n2:
    c.append(arr2[j])
    j+=1

print(*c)