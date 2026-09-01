def countNonLeap(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 0
    left=countNonLeap(root.left)
    right=countNonLeap(root.right)
    return left+right+1