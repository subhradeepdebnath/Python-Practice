def func(arr):
    a=[]
    for i in range(len(arr)):
        if arr[i] in a:
            continue
        count=0
        for j in range(len(arr)):
            if arr[i]==arr[j]:
                count+=1
        a.append([arr[i],count])
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i][1]<a[j][1]:
                temp=a[i]
                a[i]=a[j]
                a[j]=temp
    b=""
    for i in range(len(a)):
        for j in range(a[i][1]):
            b=b+a[i][0]
    print(b)
arr=input()
func(arr)