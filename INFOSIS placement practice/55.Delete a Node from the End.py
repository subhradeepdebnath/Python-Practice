# Delete a Node from the End
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next=None
temp=head
while temp!=None:
    print(temp.data)
    temp=temp.next
    