def enqueue(queue,value):
    queue.append( value)
arr=list(map(int, input().split()))
value=int(input())
queue=[]
for i in range(len(arr)):
    queue.append(arr[i])
enqueue(queue,value)
print(queue)