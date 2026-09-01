# Check Whether Two Arrays Are Equal After Sorting
arr1=list(map(int, input().split()))
arr2=list(map(int, input().split()))
arr1.sort()
arr2.sort()

if arr1 == arr2:
    print("equal")
else:
    print("not equal")