def is_empty(stack):
    if len(stack)==0:
        return True
    else:
        return False
stack=[]
arr=list(map(int, input().split()))
for i in range(len(arr)):
    stack.append(arr[i])
if is_empty(stack):
    print("empty")
else:
    print("not empty")