def func(arr):
    intervals=[]
    for i in range(0,len(arr),2):
        intervals.append([arr[i],arr[i+1]])
    intervals.sort()
    a=[intervals[0]]
    for i in range(1,len(intervals)):
        if intervals[i][0]<=a[-1][1]:
            if intervals[i][1]>a[-1][1]:
                a[-1][1]=intervals[i][1]
        else:
            a.append(intervals[i])
    print(a)
arr=list(map(int, input().split()))
func(arr)