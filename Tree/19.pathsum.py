def pathSum(root, target):
    if root is None:
        return False

    if root.left is None and root.right is None:
        return target == root.data

    return pathSum(root.left, target - root.data) or pathSum(root.right, target - root.data)