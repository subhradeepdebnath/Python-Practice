class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
def delete(head):
    if head==None:
        return None
    if head.next==None:
        return None
    temp=head
    while temp.next.next!=None:
        temp=temp.next
    temp.next=None
    return head
def traverse(head):
    temp = head
    while temp != None:
        print(temp.data)
        temp = temp.next
head = delete(head)
traverse(head)