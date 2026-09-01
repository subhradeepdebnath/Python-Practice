class node:
    def __init__(self,data):
        self.data=data
        self.next=None
found=False
search=30
n1=node(10)
n2=node(20)
n3=node(30)
n4=node(40)
n1.next=n2
n2.next=n3
n3.next=n4
current=n1
while current!=None:
    if current.data==search:
        found=True
        break
    current=current.next
if found:
    print("found")
else:
    print("not found")