def invert(root):
    if root is None:
        return 0
    temp=root.left
    root.left=root.right
    root.right=temp
    invert(root.left)
    invert(root.right)
    return root