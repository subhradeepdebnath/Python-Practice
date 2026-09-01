# insert at end?
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
first=Node(10)
second=Node(20)
third=Node(30)
first.next=second
second.next=third
new=Node(40)
third.next=new
temp=first
while temp!=None:
    print(temp.data)
    temp=temp.next

    