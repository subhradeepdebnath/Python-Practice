# Print all even numbers from 1 to N?
n=int(input())
a=[]
for i in range(1,n+1):
    if i %2==0:
        a.append(i)
for i in a:
    print(i)