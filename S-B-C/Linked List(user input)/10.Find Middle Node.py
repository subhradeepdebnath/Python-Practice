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
slow=head
fast=head
while fast!=None and fast.next!=None:
    slow=slow.next
    fast=fast.next.next
current=head

while current!=None:
    print(slow.data,end="")
    break
current=current.next