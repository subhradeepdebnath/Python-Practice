arr1=list(map(int, input().split()))
arr2=list(map(int, input().split()))
arr1.sort()
arr2.sort()
if len(arr1)!=len(arr2):
    print("not equal")
else:
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            print("not equal")
            break
    else:
        print("equal")