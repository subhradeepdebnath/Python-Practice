def dequeue(queue):
    if len(queue)==0:
        return -1
    else:
        return queue.pop(0)
arr=list(map(int , input().split()))
queue=[]
for i in range(len(arr)):
    queue.append(arr[i])
removed=dequeue(queue)
print(removed)
print(queue)