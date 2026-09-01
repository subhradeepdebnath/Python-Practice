class node:
    def __init__(self,data):
        self.data=data
        self.next=None
arr=list(map(int, input().split()))
value=int(input())
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

newNode=node(value)
newNode.next=head
head=newNode

current=head
while current!=None:
    print(current.data, end="")
    current=current.next
    if current!=None:
        print("->", end="")