def countNodes(root):
    if root is None:
        return 0
    left=countNodes(root.left)
    right=countNodes(root.right)
    return left+right+1