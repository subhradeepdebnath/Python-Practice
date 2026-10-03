def func(arr,ar):

    if len(arr)!=len(ar):

        print("false")
        return

    a={}
    b={}

    for i in range(len(arr)):

        if arr[i] in a:

            if a[arr[i]]!=ar[i]:
                print("false")
                return

        else:

            a[arr[i]]=ar[i]

        if ar[i] in b:

            if b[ar[i]]!=arr[i]:
                print("false")
                return

        else:

            b[ar[i]]=arr[i]

    print("true")


arr=input()

ar=input()

func(arr,ar)