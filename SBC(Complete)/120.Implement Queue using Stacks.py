def func(arr):
    stack1=[]
    stack2=[]
    for i in range(len(arr)):
        stack1.append(arr[i])
    while len(stack1)>0:
        stack2.append(stack1.pop())
    while len(stack2)>0:
        print(stack2.pop())
arr=list(map(int, input().split()))
func(arr)
    