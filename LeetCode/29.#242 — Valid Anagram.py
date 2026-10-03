def func(arr,ar):
    a=sorted(arr)
    b=sorted(ar)
    if a==b:
        print("anagram")
    else:
        print("not anagram")
    
arr=input()
ar=input()
func(arr,ar)