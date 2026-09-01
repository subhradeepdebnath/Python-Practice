# First and Last Occurrence of an Element
# First and Last Occurrence of an Element

n=int(input())
arr=list(map(int,input().split()))
x=int(input())

first=-1
last=-1

for i in range(n):
    if arr[i]==x:
        if first==-1:
            first=i
        last=i

print(first,last)