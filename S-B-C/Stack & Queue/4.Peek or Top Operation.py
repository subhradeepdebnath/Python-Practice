def top(stack):
    if len(stack)==0:
        return -1
    else:
        return stack[-1]
stack=[]
arr=list(map(int, input().split()))
for i in range(len(arr)):
    stack.append(arr[i])
toop=top(stack)
print(toop)
print(stack)