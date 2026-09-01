class node:
    def __init__(self, data):
        self.data=data
        self.next=None
count=0
n1=node(10)
n2=node(20)
n3=node(30)
n4=node(40)
n1.next=n2
n2.next=n3
n3.next=n4
current=n1
while current!=None:
    count+=1
    current=current.next
print(count)