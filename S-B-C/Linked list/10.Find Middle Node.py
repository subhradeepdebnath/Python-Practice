class node:
    def __init__(self,data):
        self.data=data
        self.next=None
n1=node(10)
n2=node(20)
n3=node(30)
n4=node(40)
n5=node(50)

n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n5

head=n1

slow=head
fast=head

while fast!=None and fast.next!=None:
    slow=slow.next
    fast=fast.next.next
print(slow.data)