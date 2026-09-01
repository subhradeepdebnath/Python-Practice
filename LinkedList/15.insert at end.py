class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
def end(head,data):
    new=Node(data)
    temp=head
    while temp.next != None:
        temp = temp.next
    temp.next = new
    return head
def traverse(head):
    temp=head
    while temp!=None:
        print(temp.data)
        temp=temp.next
head=end(head,40)
traverse(head) 