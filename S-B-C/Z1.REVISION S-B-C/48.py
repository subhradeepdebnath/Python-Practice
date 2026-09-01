def func(s):
    stack=[]
    for ch in s:
        stack.append(ch)
    ans=""
    while stack:
        ans+=stack.pop()
    print(ans)
s=input()
func(s)
