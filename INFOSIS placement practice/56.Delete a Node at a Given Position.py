# Delete a Node at a Given Position
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(40)
head.next.next=head.next.next.next
temp=head
while temp!=None:
    print(temp.data)
    temp=temp.next
    