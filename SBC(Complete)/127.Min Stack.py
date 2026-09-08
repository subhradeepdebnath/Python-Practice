def func(arr):
    stack=[]
    for i in range(len(arr)):
        stack.append(arr[i])
    stack.sort()
    print(stack[0])
arr=list(map(int, input().split()))
func(arr)