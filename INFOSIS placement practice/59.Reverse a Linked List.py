# Reverse a Linked List
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
prev=None
current=head
while current!=None:
    next=current.next
    current.next=prev
    prev=current
    current=next
head=prev
temp=head
while temp!=None:
    print(temp.data)
    temp=temp.next