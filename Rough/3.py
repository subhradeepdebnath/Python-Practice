# valid anagrams
def func(s,n):
    m=sorted(s)
    p=sorted(n)
    if m==p:
        print("anagram")
    else:
        print("not")
s=input()
n=input()
func(s,n)