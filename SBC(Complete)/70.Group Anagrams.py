def func(arr):

    used=[]

    for i in range(len(arr)):

        if arr[i] in used:
            continue

        a=sorted(arr[i])
        print(arr[i], end=" ")

        for j in range(i+1,len(arr)):
            b=sorted(arr[j])

            if a==b:
                print(arr[j], end=" ")
                used.append(arr[j])

        used.append(arr[i])
        print()


arr=input().split()
func(arr)