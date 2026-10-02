def func(s,target):
    for i in range(len(s)):
        if target in s[i:i+len(target)]:
            print(i)
            return
    print(-1)
s=input()
target=input()
func(s,target)