arr=list(map(int, input().split()))
count=0
cout=0
for i in range(len(arr)):
    if arr[i]%2==0:
        count+=1
    else:
        cout+=1
print("even", count)
print("odd", cout)