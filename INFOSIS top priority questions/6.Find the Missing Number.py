# Find the Missing Number
n=int(input())
arr=list(map(int, input().split()))
arr.sort()
num=[]
for i in range(n-1):
    if arr[i]!= i+1:
        print(i+1)
        break
else:
    print(n)