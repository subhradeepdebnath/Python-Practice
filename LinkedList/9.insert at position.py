# insert at position
class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
first=Node(10)
second=Node(20)
third=Node(30)
first.next=second
second.next=third
new=Node(15)
first.next=new
new.next=second
temp=first
while temp!=None:
    print(temp.data)
    temp=temp.next