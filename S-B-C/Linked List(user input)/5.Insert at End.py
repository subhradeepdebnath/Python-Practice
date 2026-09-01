class node:
    def __init__(self,data):
        self.data=data
        self.next=None
arr=list(map(int, input().split()))
val=int(input())
head=None
current=None
for i in range(len(arr)):
    newNode=node(arr[i])
    if head==None:
        head=newNode
        current=newNode
    else:
        current.next=newNode
        current=newNode
newNode=node(val)
current=head
while current.next!=None:
    current=current.next
current.next=newNode

current=head
while current!=None:
    print(current.data)
    current=current.next
    