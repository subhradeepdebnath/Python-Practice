def LCA(root,p,q):
    if root is None:
        return None
    if root.data==p or root.data==q:
        return root
    left=LCA(root.left,p,q)
    right=LCA(root.right,p,q)
    if left and right:
        return root
    if left:
        return left
    if right:
        return right