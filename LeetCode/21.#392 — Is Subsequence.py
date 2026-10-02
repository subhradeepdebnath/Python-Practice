def func(arr,target):
    j=0
    for ch in arr:
        if j<len(target) and ch == target[j]:
            j=j+1
    if j==len(target):
        print("true")
    else:
        print("false")
target=input()
arr=input()
func(arr,target)