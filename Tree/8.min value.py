def minValue(root):
    if root is None:
        return 0
    left=minValue(root.left)
    right=minValue(root.right)
    return min(left,right,root.data)