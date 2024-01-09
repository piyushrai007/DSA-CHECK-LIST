class heap:
    def __init__(self):
        self.arr =[0]*100
        self.size = 0 
        self.arr[0]=-1
    def insetion(self,val):
        self.size = self.size+1
        index = self.size
        self.arr[index] =val
        while index>1:
            parent = index//2
            if self.arr[parent]<self.arr[index]:
                temp  = self.arr[parent]
                self.arr[parent] = self.arr[index]
                self.arr[index] = temp
            else:
                return None
    def deletion(self):
        if self.size ==0:
            print("noting to dlt")

        else:
            self.arr[1] = self.arr[self.size]    
            self.size-=1

            i = 1
            while i <self.size:
                lc =2*i
                rc =2*i+1
                if lc < self.size and self.arr[i]<self.arr[lc]:
                    temp  = self.arr[i]
                    self.arr[i] = self.arr[lc]
                    self.arr[lc] = temp
                elif rc < self.size and self.arr[i]<self.arr[rc]:
                    temp  = self.arr[i]
                    self.arr[i] = self.arr[rc]
                    self.arr[rc] = temp

                else:
                    return None
    def print(self):
        for i in range(1,self.size+1):
            print(self.arr[i])

def heapify(arr,n,i):
    largest = i
    left = 2*i
    right = 2*i+1
    if left <=n and arr[largest]<arr[left]:
        largest = left
    if right <=n and arr[largest]<arr[right]:
        largest = right   
    if largest!=i:
        temp = arr[largest]
        arr[largest]= arr[i]
        arr[i]=temp    
        heapify(arr,n,largest)
# h = heap()
# h.insetion(50)
# h.insetion(55)
# h.insetion(53)
# h.insetion(52)
# h.insetion(54)
# h.deletion()

# h.print()
# arr = [-1,54,53,55,52,50]
# n = 5
# for i in range((n//2)+1,0,-1):
#     print(i)
#     heapify(arr,n,i)
# print(arr)    


