s=input()
arr=s.split()
long=arr[0]
for i in range(len(arr)):
    if len(arr[i])>len(long):
        long= arr[i]
print(long)