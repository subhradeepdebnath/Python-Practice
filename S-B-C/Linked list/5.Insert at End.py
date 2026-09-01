class node:
    def __init__(self,data):
        self.data=data
        self.next=None
n1=node(10)
n2=node(20)
n3=node(30)
newNode=node(40)
n1.next=n2
n2.next=n3
n3.next=newNode
head=n1
current=head
while current!=None:
    print(current.data)
    current=current.next
