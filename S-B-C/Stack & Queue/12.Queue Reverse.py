def reverse(queue):
    queue.reverse()
arr=list(map(int, input().split()))
queue=[]
for i in range(len(arr)):
    queue.append(arr[i])
reverse(queue)
print(queue)