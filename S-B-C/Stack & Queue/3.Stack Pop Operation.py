def pop(stack):
    if len(stack)==0:
        return -1
    else:
        return stack.pop()
stack=[]
arr=list(map(int, input().split()))
for i in range(len(arr)):
    stack.append(arr[i])
removed=stack.pop()
print(removed)
print(stack)