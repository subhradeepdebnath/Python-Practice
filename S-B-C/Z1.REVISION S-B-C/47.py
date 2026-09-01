def func(arr):
    stack=[]
    for i in arr:
        stack.append(i)
    print(stack)
    x=stack.pop()
    print(x)
    print(stack)
arr=list(map(int, input().split()))
func(arr)