class node:
    def __init__(self,data):
        self.data=data
        self.next=None

arr=list(map(int,input().split()))
value=int(input())
position=int(input())

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

# Insert
newNode=node(value)
current=head

for i in range(1,position):
    current=current.next

newNode.next=current.next
current.next=newNode

# Print
current=head

while current!=None:
    print(current.data,end="")

    current=current.next

    if current!=None:
        print("->",end="")