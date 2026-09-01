# Insert a Node at the End
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
new=Node(5)
new.next=None
head.next.next.next=new
temp=head
while temp!=None:
    print(temp.data)
    temp=temp.next
    