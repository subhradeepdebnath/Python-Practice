def isBalanced(root):
    if root is None:
        return True        
    def height(node):
        if node is None:
            return 0
        left=height(node.left)
        right=height(node.right)
        return 1+max(left, right)
    left=height(root.left)
    right=height(root.right)
    if abs(left-right)>1:
        return False
    return True