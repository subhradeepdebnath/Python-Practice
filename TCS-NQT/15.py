#  given two strings, check whether they are anagrams of each other?
a=input()
b=input()
c=sorted(a)
d=sorted(b)
if c==d:
    print("anagrams")
else:
    print("not anagram")