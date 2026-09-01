# Remove Duplicates from a Sorted Linked List
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

head=Node(10)
head.next=Node(10)
head.next.next=Node(20)
head.next.next.next=Node(20)
head.next.next.next.next=Node(30)


temp=head

while temp!=None and temp.next!=None:
    if temp.data==temp.next.data:
        temp.next=temp.next.next
    else:
        temp=temp.next


while head!=None:
    print(head.data,end=" ")
    head=head.next