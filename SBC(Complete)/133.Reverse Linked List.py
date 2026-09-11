class node:
    def __init__(self,data):
        self.data=data
        self.next=None
arr=list(map(int, input().split()))
head=node(arr[0])
current=head
for i in range(1,len(arr)):
    current.next=node(arr[i])
    current=current.next
previous=None
current=head
while current!=None:
    nextnode=current.next
    current.next=previous
    previous=current
    current=nextnode
head=previous
current=head
while current!=None:
    print(current.data, end=" ")
    current=current.next
    