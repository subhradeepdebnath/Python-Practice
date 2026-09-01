class node:
    def __init__(self,data):
        self.data=data
        self.next=None
arr=list(map(int, input().split()))
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
current=head
while current.next.next!=None:
    current=current.next
current.next=None
current=head
while current!=None:
    print(current.data)
    current=current.next
    