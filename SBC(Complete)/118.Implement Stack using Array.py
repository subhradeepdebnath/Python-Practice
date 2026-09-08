def func(arr):
    stack=[]
    for i in range(len(arr)):
        stack.append(arr[i])
    print(stack)
    print(stack.pop())
    print(stack)
arr=list(map(int, input().split()))
func(arr)