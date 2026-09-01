#  check for strong number?
n=int(input())
m=str(n)
add=0
for i in m:
    fact=1
    for j in range(1,int(i)+1):
        fact*=j
    add+=fact
if n==add:
    print("strong number")
else:
    print("Not a strong number")