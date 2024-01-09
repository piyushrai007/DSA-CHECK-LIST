class Node:
    def __init__ (self, data):
        self.data = data 
        self.next = None
class SLL:
    def __init__(self): 
        self.head = None
    
    def display(self):
        if self.head is None:
            print("empty link ed-list")
        else:
            temp = self.head
            while temp:
                print(temp.data,"->" ,end=" ")
                temp = temp.next 
    def deletfirst(self):
        if self.head == None:
            print("list is empty")
        else:
            self.head = self.head.next
    def insertfist(self,value):
        newnode = Node(value)
        temp = self.head
        newnode.next =  temp
        self.head = newnode
    def insertat(self,pos,val):
        newnode = Node(val)
        temp = self.head
        try:
            for i in range(pos-1):
                temp = temp.next
            temp2 = temp.next
            temp.next = newnode
            newnode.next = temp2
        except:
            print("out of range")
    def insertlast(self,value):
        newnode = Node(value)
        if self.head == None:
            self.head =  newnode
        else:
            temp = self.head
            while temp.next != None:
                temp =  temp.next
            temp.next =  newnode 

        
l = SLL()
l.insertlast(50)   
l.insertlast(60)
l.display()
print()
l.insertfist(55)
l.display()
l.insertat(3,65)
print( )
l.display()


           
    