# Given an integer array arr, determine whether the array contains any duplicate element.
n=int(input())
arr=list(map(int, input().split()))
c=[]
for i in arr:
    if i in c:
        print(True)
        break
    else:
        c.append(i)
else:
    print(False)