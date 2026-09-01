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
max=head.data
current=head
while current!=None:
    if current.data> max:
        max=current.data
    current=current.next
print(max)