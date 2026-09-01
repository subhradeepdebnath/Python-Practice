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
prev=None
current=head

while current!=None:
    next=current.next
    current.next=prev
    prev=current
    current=next
head=prev

current=head

while current!=None:
    print(current.data,end="")

    current=current.next

    if current!=None:
        print("->",end="")