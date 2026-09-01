def search(root, key):
    if root is None:
        return False
    if root.data==key:
        return True
    left=search(root.left, key)
    right=search(root.right, key)
    return left or right