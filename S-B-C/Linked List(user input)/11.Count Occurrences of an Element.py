class node:
    def __init__(self,data):
        self.data=data
        self.next=None

arr=list(map(int,input().split()))
target=int(input())
head=None
current=None

for i in range(len(arr)):
    newNode=node(arr[i])

    if head==None:
        head=newNode
        current=newNode
    else:
        current.next=newNode
        current=newNode
count=0

current=head
while current!=None:
    if current.data==target:
        count+=1
    current=current.next
print(count)