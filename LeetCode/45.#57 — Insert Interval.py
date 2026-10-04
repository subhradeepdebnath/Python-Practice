def func(arr,new):
    intervals=[]
    for i in range(0,len(arr),2):
        intervals.append([arr[i],arr[i+1]])       # 2 numbers ko ek interval banao
    intervals.append(new)                         # new interval bhi add karo
    intervals.sort()                              # sab intervals ko start ke according sort karo

    a=[intervals[0]]                              # pehla interval answer mein daalo

    for i in range(1,len(intervals)):
        if intervals[i][0]<=a[-1][1]:             # overlap ho raha hai
            if intervals[i][1]>a[-1][1]:          # current end bada hai
                a[-1][1]=intervals[i][1]         # last interval ka end update karo
        else:
            a.append(intervals[i])                # overlap nahi hai, new interval add karo

    print(a)

arr=list(map(int,input().split()))
new=list(map(int,input().split()))
func(arr,new)