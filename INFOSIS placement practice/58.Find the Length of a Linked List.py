# Find the Length of a Linked List
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
count=0
temp=head
while temp!=None:
    count+=1
    temp=temp.next
print(count)