def func(arr):
    pos=0
    neg=0
    zero=0
    for i in range(len(arr)):
        if arr[i]>0:
            pos+=1
        elif arr[i]<0:
            neg+=1
        else:
            zero+=1
    print("positivie:", pos)
    print("negative:", neg)
    print("Zero:", zero)
arr=list(map(int, input().split()))
func(arr)
    