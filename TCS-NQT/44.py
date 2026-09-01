#  given an array,count how many even and odd numbers are there in Array?
n=int(input())
arr=list(map(int, input().split()))
e_count=0
o_count=0
for i in arr:
    if i%2==0:
        e_count+=1
    else:
        o_count+=1
print(e_count)
print(o_count)