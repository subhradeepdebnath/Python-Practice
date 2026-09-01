#  given a base and an exponent, find the value of power?
num=int(input())
pow=int(input())
res=1
for i in range(pow):
    res=res*num
print(res)