def maxdepth(root):
    if root is None:
        return 0
    left=maxdepth(root.left)
    right=maxdepth(root.right)
    return 1+max(left,right)