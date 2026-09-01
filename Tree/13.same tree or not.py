def sameTree(root1,root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    if root1.data!=root2.data:
        return False
    left=sameTree(root1.left,root2.left)
    right=sameTree(root1.right,root2.right)
    return left and right