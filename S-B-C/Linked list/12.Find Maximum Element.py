class node:
    def __init__(self,data):
        self.data=data
        self.next=None
n1=node(10)
n2=node(20)
n3=node(30)
n4=node(60)
n5=node(55)

n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n5

head=n1
max=head.data
current=head
while current!=None:
    if current.data>max:
        max=current.data
    current=current.next
print(max)