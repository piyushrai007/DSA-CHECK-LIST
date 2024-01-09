class Queue:
    def __init__(self,size):
        self.size = size
        self.items = [None]*size
        self.r =0
        self.f = 0
    def is_empty(self):
        return self.f ==self.r
    def is_full(self):
        return self.r==self.size

    def enqueue(self, item):
        if self.is_full():
            print("queue is full")    
        else:
            self.items[self.r]=item
            self.r+=1
            print("enque is elt",item,"sucessfully")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
        else:
            ans = self.items[self.f]
            self.items[self.f] = -1
            self.f+=1
            if self.f ==self.r:
                self.f = 0
                self.r =0
            print("dequeue of",ans,"sucessfully")        
        


a = Queue(3)
# print(a.isEmpty)        
a.dequeue()
a.enqueue(45)
a.dequeue()
a.enqueue(45)
a.enqueue(45)
a.enqueue(47)
a.enqueue(45)


    