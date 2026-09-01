#  given a binary number, convert it to decimal?
n=int(input())
m=str(n)[::-1]
power=0
add=0
for i in m:
    val=int(i)*(2**power)
    add=add+val
    power+=1
print(add)