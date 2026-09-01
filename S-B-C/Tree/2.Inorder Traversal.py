class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inorder(root):
    if root == None:
        return

    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)


arr = list(map(int, input().split()))

root = node(arr[0])

queue = [root]
i = 1

while i < len(arr):

    current = queue.pop(0)

    if arr[i] != -1:
        current.left = node(arr[i])
        queue.append(current.left)

    i += 1

    if i < len(arr) and arr[i] != -1:
        current.right = node(arr[i])
        queue.append(current.right)

    i += 1


inorder(root)