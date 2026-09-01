def display(queue):
    for i in range(len(queue)):
        print(queue[i],end=" ")
arr=list(map(int, input().split()))
queue=[]
for i in range(len(arr)):
    queue.append(arr[i])
display(queue)