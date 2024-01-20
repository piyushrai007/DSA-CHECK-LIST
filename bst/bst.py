class bst:
    def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
    def insert(self,data):
        if data == self.data:
            return
        if data < self.data:
            
            #left
            if self.left:
                self.left.insert(data)
            else:
                self.left = bst(data)
        if data >self.data:
            #right
            if self.right:
                self.right.insert(data)
            else:
                self.right = bst(data)
    def inorder_show(self):
        if self == None:
            return -1
        if self.left:
            self.left.inorder_show()
        print(self.data)
        if self.right:
            self.right.inorder_show()
    def postorder(self):
        if self == None:
            return -1
        if self.right:
            self.right.inorder_show()
        
        print(self.data)
        if self.left:
            self.left.inorder_show()

    def preorder(self):
        if self == None:
            return
        print(self.data)
        if self.left:
            self.left.inorder_show()
        if self.right:
            self.right.inorder_show()

    def search (self, val):
        if self.data == val:
            return True
        if val< self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val> self.data:
            if self.right:
                return self.right.search(val)
            else:
                return false
    def find_max(self):
        if self.right == None:
            return self.data
        else:
            return self.right.find_max()

    def find_min(self):
        if self.left == None:
            return self.data
        else:
            return self.left.find_max()
    def delet(self,val):
        if val < self.data:
            if self.left:
                self.left=self.left.delet(val)
        elif val>self.data:
            if self.right:
                self.right=self.right.delet(val)
        else:
            if self.right and self.left is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)
        return self

        
        
a = bst(10)
a.insert(5)
a.insert(15)
# for i in range(50,30,-1):
#     a.insert(i)
# a.inorder_show()
a.preorder()
a.inorder_show()
print("postorder")
a.postorder()