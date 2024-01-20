class Solution(object):
    def __init__(self):
        self.prev = None
    def isValidBST(self, root):
        if root is None:
            return True  # Empty tree is considered a valid BST
        if not self.isValidBST(root.left):
            return False
        if self.prev is not None and root.val <= self.prev.val:
            return False
        self.prev = root
        return self.isValidBST(root.right)