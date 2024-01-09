
class Solution:
    #Function to return the level order traversal of a tree.
    def levelOrder(self,root ):
        ans= []
        if not root:
            return ans
        new = Node
        qe =[]
        qe.append(root)
        while qe:
            size = len(qe)
            # level = []
            for i in range(size):
                new = qe[0]
                qe.pop(0)
                if new.left:
                    qe.append(new.left)
                if new.right:
                    qe.append(new.right)   
                # level.append(new.data) 
                ans.append(new.data)    
        return ans