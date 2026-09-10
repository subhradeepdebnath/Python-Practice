class node:
    def __init__(self,data):
        self.data=data
        self.next=None
arr=list(map(int, input().split()))
head=node(arr[0])
current=head
for i in range(1,len(arr)):
    current.next=node(arr[i])
    current=current.next
current=head
while current!=None:
    print(current.data, end=" ")
    current=current.next
    