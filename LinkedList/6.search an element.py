# Search an element?
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None  
first= Node(10)
second=Node(20)
third=Node(30)
first.next=second
second.next=third
key=20
found=False
temp=first
while temp!= None:
    if temp.data==key:
        found=True
        break
    temp=temp.next
if found:
    print("Found")
else:
    print("Not Found")
    