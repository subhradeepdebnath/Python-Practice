def maxValue(root):
    if root is None:
        return 0
    left=maxValue(root.left)
    right=maxValue(root.right)
    return max(left,right,root.data)