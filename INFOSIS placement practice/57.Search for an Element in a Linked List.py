# Search for an Element in a Linked List
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(40)
key=30
temp=head
found=False
while temp!=None:
    if temp.data ==key:
        found=True
        break
    temp=temp.next
if found:
    print("found")
else:
    print("Not found")    