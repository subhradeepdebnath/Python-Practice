def func(arr):
    queue=[]
    for i in range(len(arr)):
        queue.append(arr[i])
    print(queue)
    print(queue.pop(0))
    print(queue)
arr=list(map(int, input().split()))
func(arr)