class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
def search(head, key):
    temp=head
    while temp!=None:
        if temp.data==key:
            return True
        temp=temp.next
    return False
print(search(head, 20))
print(search(head, 50))