#  delete at the end
class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
first=Node(10)
second=Node(20)
third=Node(30)
first.next=second
second.next=third
second.next=None
temp=first
while temp!=None:
    print(temp.data)
    temp=temp.next