class node:
    def __init__(self,data):
        self.data=data
        self.next=None

arr=list(map(int,input().split()))

head=None
current=None

value=int(input())

for i in range(len(arr)):
    newNode=node(arr[i])

    if head==None:
        head=newNode
        current=newNode
    else:
        current.next=newNode
        current=newNode

current=head

while current.next.data != value:
    current=current.next

current.next=current.next.next

current=head

while current!=None:
    print(current.data)
    current=current.next