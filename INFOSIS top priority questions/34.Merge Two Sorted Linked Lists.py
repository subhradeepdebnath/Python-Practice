class  Node:
    def __init__(self,data):
        self.data=data
        self.next=next
head1=Node(10)
head1.next=Node(20)
head1.next.next=Node(30)

head2=Node(10)
head2.next=Node(20)
head2.next.next=Node(30)

def merge(head1,head2):
    temp=Node(0)
    curr=temp

    while head1 and head2:
        if head1.data < head2.data:
            curr.next=head1
            head1=head1.next
        else:
            curr.next=head2
            head2=head2.next

        curr=curr.next

    if head1:
        curr.next=head1
    else:
        curr.next=head2

    return temp.next


head=merge(head1,head2)
    print(head.data,end=" ")
    head=head.next