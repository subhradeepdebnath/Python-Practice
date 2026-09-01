n=int(input())
arr=input().split()

prefix=arr[0]

for i in range(1,n):
    while not arr[i].startswith(prefix):
        prefix=prefix[:-1]
        if prefix=="":
            break

if prefix=="":
    print(-1)
else:
    print(prefix)