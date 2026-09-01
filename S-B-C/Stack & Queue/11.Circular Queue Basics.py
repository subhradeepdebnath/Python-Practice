def enqueue(queue,value, rear, size):
    if rear==size-1:
        rear=0
    else:
        rear=rear+1
    queue[rear]=value
    return rear
size=int(input())
queue=[0]*size
rear=-1
arr=list(map(int, input().split()))
for i in range(len(arr)):
    rear=enqueue(queue,arr[i],rear,size)
print(queue)

