#  make a node class, and print 10?
class Node:
    def __init__(self, data):
        self.data = data
        self.next=None
obj=Node(10)     
print(obj.data)