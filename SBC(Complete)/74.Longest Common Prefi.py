def func(arr):

    prefix=arr[0]

    for i in range(1,len(arr)):
        j=0
        temp=""

        while j<len(prefix) and j<len(arr[i]) and prefix[j]==arr[i][j]:
            temp=temp+prefix[j]
            j+=1

        prefix=temp

    print(prefix)

arr=input().split()
func(arr)