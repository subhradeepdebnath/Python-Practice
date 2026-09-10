class node:
    def __init__(self,data):
        self.data=data
        self.next=None

arr=list(map(int, input().split()))
position=int(input())
value=int(input())

head=node(arr[0])
current=head

for i in range(1,len(arr)):
    current.next=node(arr[i])
    current=current.next

newnode=node(value)

if position==1:
    newnode.next=head
    head=newnode
else:
    current=head
    for i in range(position-2):
        current=current.next
    newnode.next=current.next
    current.next=newnode

current=head
while current!=None:
    print(current.data,end=" ")
    current=current.next