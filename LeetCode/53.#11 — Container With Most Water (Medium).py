def func(arr):
    i=0
    j=len(arr)-1
    maxi=0
    while i<j:
        h=min(arr[i],arr[j])
        width=j-i
        area=h*width
        if area>maxi:
            maxi=area
        if arr[i]<arr[j]:
            i+=1
        else:
            j-=1
    print(maxi)
arr=list(map(int, input().split()))
func(arr)