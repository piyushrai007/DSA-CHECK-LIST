def lcr(root,a,b):
    c = root.data
    if root==null:return None
    if a==c and b==c:
        return root
    root.left = lccr(root.left,a,b)
    root.right = lccr(right.left,a,b)
    if root.left == None :return right
    if root.right ==None :return left
    return root 