def func(arr):
    queue=[]
    for i in range(len(arr)):
        queue.append(arr[i])
    stack=[]
    while len(queue)>0:
        stack.append(queue.pop(0))
    while len(stack)>0:
        print(stack.pop())
arr=list(map(int, input().split()))
func(arr)