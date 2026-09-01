n=int(input())
arr=list(map(int, input().split()))
e_sum=0
o_sum=0
for i in range(n):
    if i%2==0:
        e_sum+=arr[i]
    else:
        o_sum+=arr[i]
print(e_sum)
print(o_sum)