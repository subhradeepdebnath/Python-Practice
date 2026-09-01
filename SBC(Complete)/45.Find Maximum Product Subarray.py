def func(arr):
    curr_max=arr[0]
    curr_min=arr[0]
    maximum=arr[0]

    for i in range(1,len(arr)):
        a=arr[i]

        p1=a
        p2=a*curr_max
        p3=a*curr_min

        curr_max=max(p1,p2,p3)
        curr_min=min(p1,p2,p3)

        if curr_max>maximum:
            maximum=curr_max

    print(maximum)


arr=list(map(int,input().split()))
func(arr)