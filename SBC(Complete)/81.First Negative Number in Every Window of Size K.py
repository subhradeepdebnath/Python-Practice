def func(arr,k):
    for i in range(len(arr)-k+1):      # Har window ka starting point
        found=0                        # Negative na mile to 0
        for j in range(i,i+k):        # Current window ke K elements
            if arr[j]<0:               # Negative number check
                found=arr[j]           # Negative number store karo
                break                  # Pehla negative mil gaya
        print(found,end=" ")           # Answer print karo
arr=list(map(int,input().split()))     # Array input
k=int(input())                          # Window size
func(arr,k)                             # Function call