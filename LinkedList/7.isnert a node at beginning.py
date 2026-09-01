# insert a node at the beginning?
class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
first=Node(10)
second=Node(20)
third=Node(30)
first.next=second
second.next=third
new=Node(5)
temp=first
new.next=first
first=new
temp=first
while temp!=None:
    print(temp.data, end=" ")
    temp=temp.next
    