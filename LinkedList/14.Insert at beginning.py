class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
def insert(head,data):
    new=Node(data)
    new.next=head
    head=new
    return head
def traverse(head):
    temp=head
    while temp!=None:
        print(temp.data)
        temp=temp.next
head=insert(head,5)
traverse(head)