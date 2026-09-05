def func(arr,k):
    for i in range(len(arr)-k+1):       
        max=arr[i]                   
        for j in range(i,i+k):        
            if arr[j]>max:              
                max=arr[j]                       
        print(max,end=" ")          
arr=list(map(int,input().split()))    
k=int(input())                        
func(arr,k)                           