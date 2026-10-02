def func(arr):
    a=[]
    for i in range(len(arr)):
        b=[]
        for j in range(len(arr)):
            if j!=i:
                if sorted(arr[i])==sorted(arr[j]):
                    b.append(arr[j])
        b.append(arr[i])
        if b not in a:
                    a.append(b)
    print(a)
arr=input().split()
func(arr)