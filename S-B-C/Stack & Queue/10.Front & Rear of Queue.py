def front(queue):
    if len(queue)==0:
        return -1
    return queue[0]
def rear(queue):
    if len(queue)==0:
        return -1
    return queue[-1]
arr=list(map(int, input().split()))
queue=[]
for i in range(len(arr)):
    queue.append(arr[i])
print("front",front(queue))
print("rear",rear(queue))