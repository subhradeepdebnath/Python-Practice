# given an array of N integer and a key,check whether the key is present in the array.
n=int(input())
arr=list(map(int, input().split()))
key=int(input())
found=False
for i in arr:
    if i==key:
        found=True
if found:
    print("found")
else:
    print("Not found")