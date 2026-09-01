class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(40)
prev=None
curr=head
while curr!=None:
    next=curr.next
    curr.next=prev
    prev=curr
    curr=next
head=prev
temp=head
while temp!=None:
    print(temp.data, end=" ")
    temp=temp.next
    