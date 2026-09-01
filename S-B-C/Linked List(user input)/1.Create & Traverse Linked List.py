# class node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# n=int(input())
# arr=list(map(int, input().split()))
# head=None
# current=None
# for i in range(n):
#     newNode=node(arr[i])
    
#     if head==None:
#         head=newNode
#         current=newNode
#     else:
#         current.next=newNode
#         current=newNode
# current=head
# while current!=None:
#     print(current.data, end=" ")
#     current=current.next
    
    
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
n=int(input())
arr=list(map(int, input().split()))
head=None
current=None
for i in range(n):
    newNode=node(arr[i])
    
    if head==None:
        head=newNode
        current=newNode
    else:
        current.next=newNode
        current=newNode
current=head
while current!=None:
    print(current.data, end=" ")
    current=current.next