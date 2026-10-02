def func(s,target):
    for i in range(len(s)):
        if s[i:i+len(target)]==target:
            print(i)
            return
    print(-1)
s=input()
target=input()
func(s,target)