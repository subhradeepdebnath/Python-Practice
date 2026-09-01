class node:
    def __init__(self,data):
        self.data=data
        self.next=None
n1=node(10)
n2=node(20)
n3=node(30)
n4=node(20)
n5=node(20)

n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n5
search=20
count=0
head=n1
current=head
while current!=None:
    if current.data==search:
        count+=1
    current=current.next
print(count)