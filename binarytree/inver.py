def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root ==  None:
            return root
        
        temp = root.left
        root.left=self.invertTree(root.right)
        root.right=self.invertTree(temp)
        return root