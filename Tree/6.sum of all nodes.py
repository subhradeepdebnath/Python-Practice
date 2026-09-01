def sumNodes(root):
    if root is None:
        return 0
    left=sumNodes(root.left)
    right=sumNodes(root.right)
    return left+right+root.data