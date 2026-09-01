def func(arr):
    queue=[]
    for i in arr:
        queue.append(i)
    front=queue[0]
    rear=queue[-1]
    print(front)
    print(rear)
arr=list(map(int, input().split()))
func(arr)
