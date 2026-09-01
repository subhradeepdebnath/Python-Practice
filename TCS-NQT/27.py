# given two arrays, merge them into a single array and print the merged array?
n=int(input())
arr=list(map(int, input().split()))
m=int(input())
arr1=list(map(int, input().split()))
new=[]
for i in arr:
    if i not in new:
        new.append(i)
        
for i in arr1:
    if i not in new:
        new.append(i)
    
print(new)