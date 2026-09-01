n=int(input())
arr=list(map(int, input().split()))
a=[]
for i in range(n-1,-1,-1):
    print(arr[i], end=" ")
    if i!=0:
        print("->",end=" ") 