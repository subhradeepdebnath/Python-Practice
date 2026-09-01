class node:
    def __init__(self,data):
        self.data=data
        self.next=None
def func(arr,pos,val):
    head=node(arr[0])
    current=head
    for i in range(1, len(arr)):
        current.next = node(arr[i])
        current= current.next
    new=node(val)
    if pos==0:
        new.next=head
        head= new
    else:
        current=head
        for i in range(pos-1):
            current=current.next
        new.next=current.next
        current.next=new
        current=head
        while current:
            print(current.data, end="")
            current=current.next
arr=list(map(int, input().split()))
pos=int(input())
val=int(input())
func(arr,pos,val)