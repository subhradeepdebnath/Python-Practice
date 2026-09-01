# Delete a Node from the Beginning
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head=head.next
temp=head
while temp!=None:
    print(temp.data)
    temp=temp.next
    