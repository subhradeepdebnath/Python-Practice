class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(40)
head.next.next.next.next=head.next
slow=head
fast=head
found=False
while fast!=None and fast.next!=None:
    slow=slow.next
    fast=fast.next.next
    if slow==fast:
        found=True
        break
if found:
    print("YES")
else:
    print("NO")