class node:
    def __init__(self,data):
        self.data=data
        self.next=None
arr=list(map(int, input().split()))
position=int(input())
head=node(arr[0])
current=head
for i in range(1,len(arr)):
    current.next=node(arr[i])
    current=current.next
if position==1:
    head=head.next
else:
    current=head
    for i in range(position-2):
        current=current.next
    current.next=current.next.next
current=head
while current!=None:
    print(current.data, end=" ")
    current=current.next
    