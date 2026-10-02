def func(arr):
    a=[]
    i=0
    while i<len(arr):
        count=1
        j=i+1
        while j<len(arr) and arr[i]==arr[j]:
            count+=1
            j+=1
        a.append(arr[i])
        if count>1:
            for ch in str(count):
                a.append(ch)
        i=j
    print(len(a))
    print(a)
arr=input()
func(arr)