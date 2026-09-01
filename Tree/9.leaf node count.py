def countLeaf(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    left=countLeaf(root.left)
    right=countLeaf(root.right)
    return left+right