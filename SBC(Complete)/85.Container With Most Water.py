def func(arr):
    maximum=0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]<arr[j]:
                height=arr[i]
            else:
                height=arr[j]
            width=j-i
            area=height*width
            if area>maximum:
                maximum=area
    print(maximum)
arr=list(map(int,input().split()))
func(arr)