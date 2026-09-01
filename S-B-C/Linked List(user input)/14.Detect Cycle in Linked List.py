class node:
    def __init__(self,data):
        self.data=data
        self.next=None

arr=list(map(int,input().split()))

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

# Create cycle
current.next=head.next

slow=head
fast=head

found=False

while fast!=None and fast.next!=None:
    slow=slow.next
    fast=fast.next.next

    if slow==fast:
        found=True
        break

if found:
    print("Cycle")
else:
    print("No Cycle")