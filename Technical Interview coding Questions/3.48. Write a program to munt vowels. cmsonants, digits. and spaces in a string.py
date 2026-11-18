def func(arr):
    v=0
    c=0
    d=0
    s=0
    for i in range(len(arr)):
        if arr[i] in "aeiouAEIOU":
            v+=1
        elif arr[i].isalpha():
            c+=1
        elif arr[i].isdigit():
            d+=1
        elif arr[i] == " ":
            s+=1
    print(v,c,d,s)
arr=input()
func(arr)