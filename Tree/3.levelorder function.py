def levelorder(root):
    if root is None:
        return 
    queue=[root]
    while queue:
        node=queue.pop(0)
        print(node.data)
        if node.left:       
            queue.append(node.left)
        if node.right:
            queue.append(node.right)  