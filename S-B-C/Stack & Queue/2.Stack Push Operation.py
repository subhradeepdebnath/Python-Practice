def push(stack,value):
    stack.append(value)
stack=[]
arr=list(map(int, input().split()))
value=int(input())
for i in range(len(arr)):
    stack.append(arr[i])
push(stack,value)
print(stack)