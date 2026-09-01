def func(s):
    left=0
    right=len(s)-1
    while left<right:
        if s[left]!=s[right]:
            print("NO")
            return 
        left+=1
        right-=1
    print("yes")
s=input()
func(s)