# Insert a Node at a Given Position.
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
new=Node(5)
temp=head
new.next=temp.next
temp.next=new
temp=head
while temp!=None:
    print(temp.data)
    temp=temp.next
    
