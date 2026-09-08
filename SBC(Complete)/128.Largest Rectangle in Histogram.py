def func(arr):
    maximum=0  
    for i in range(len(arr)):
        height=arr[i]  
        for j in range(i,len(arr)):
            height=min(height,arr[j])  
            width=j-i+1  
            area=height*width  
            if area>maximum: 
                maximum=area   
    print(maximum)

arr=list(map(int,input().split()))   
func(arr)