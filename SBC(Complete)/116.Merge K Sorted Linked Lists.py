def func(arr1,arr2,arr3):
    a=[]
    for i in range(len(arr1)):
        a.append(arr1[i])
    for i in range(len(arr2)):
            a.append(arr2[i])
    for i in range(len(arr3)):
            a.append(arr3[i])
    a.sort()
    print(*a,sep="->")
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
arr3=list(map(int,input().split()))
func(arr1,arr2,arr3)