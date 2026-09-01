class node:
    def __init__(self, data):
        self.data=data
        self.next=None
def func(arr):
    head=node(arr[0])
    current=head
    for i in range(1,len(arr)):
        current.next=node(arr[i])
        current=current.next
    current=head
    while current:
        print(current.data, end=" ")
        current=current.next
arr=list(map(int, input().split()))
func(arr)
