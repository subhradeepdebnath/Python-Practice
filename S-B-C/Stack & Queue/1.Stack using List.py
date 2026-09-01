def display(stack):
    for i in range(len(stack)):
        print(stack[i], end=" ")
arr=list(map(int, input().split()))
stack=[]
for i in range(len(arr)):
    stack.append(arr[i])
display(stack)