def func(a,b):
    A=sorted(a)
    B=sorted(b)
    if A==B:
        print("anagran")
        return
    print("not anagram")
a=input()
b=input()
func(a,b)