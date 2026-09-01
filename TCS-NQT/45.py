#  find intersection between two arrays.
# given two arrays , print the common elements present in both the arrays?
n= int (input())
m=int(input())
arr1=list(map(int, input().split()))
arr2=list(map(int, input().split()))
x=[]
for i in arr1:
    if i in arr2:
        x.append(i)
print(x)