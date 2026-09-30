def func(arr):

    arr.sort()                          # Array ko ascending order mein sort karo

    min=arr[1]-arr[0]                   # Pehle pair ka difference

    for i in range(len(arr)-1):         # Adjacent pairs check karo

        difference=arr[i+1]-arr[i]      # Current pair ka difference

        if difference<min:              # Agar difference chhota hai
            min=difference               # Minimum update karo

    print(min)                          # Final minimum difference

arr=list(map(int,input().split()))

func(arr)