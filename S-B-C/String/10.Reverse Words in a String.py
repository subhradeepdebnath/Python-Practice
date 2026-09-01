s=input()
arr=s.split()
a=""
for i in range(len(arr)-1,-1,-1):
    a=a+arr[i] + " "
print(a)