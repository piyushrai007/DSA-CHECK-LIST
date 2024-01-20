import random
class Node:
    def __init__(self,data):
        self.right = None
        self.left = None
        self.data = data
    # def show(self):
    #     if self.left:
    #         self.left.show()
    #     print(self.data)
    #     if self.right:
    #         self.right.show()
class bt:
    def __init__(self,data):
        self.root = Node(data)
    def insert(self,r,data):
        if data == self.root.data:
            return
            #left
        if r ==0:
            if self.root.left:
                self.root.left.insert(data)
            else:
                self.root.left = bt(data)
        #right
        else:
            if self.root.right:
                self.right.insert(data)
            else:
                self.root.right = bt(data)
    def inorder_show(self):
        
        if self == None:
            return -1
        if self.root.left:
            self.root.left.inorder_show()
        print(self.root.data,end  =" ")

        if self.root.right:
            self.root.right.inorder_show()   
    def preorder(self):
        pass
    def level_order(self):
        if self == None:
            return -1
        else:
            a =[]
            a.append(self.root)
            while a:
              self.root = a.pop(0)
              print("levelorder",self.root.data)
              if self.root.left:
                a.append(self.root.left.root)
              if self.root.right:
                a.append(self.root.right.root) 

            
a = bt(45)
a.insert(0,66)
a.insert(9,44)
a.inorder_show()
a.level_order()




        