class dictionary:
    class node:
        def __init__(self,key ,value):
            self.key  = key
            self.value = value
            self.hash = key%7
            self.next = None
    def __init__(self):
        self.hashtable= [-1]*7
    def put(self, key, value):
        a = self.node(key,value)
        z =  key%7
        if self.hashtable[z] == -1:
            self.hashtable[z] = a
        else:
            # Traverse the linked list to check for existing keys
            current = self.hashtable[z]
            while current:
                # If the key already exists, update the value
                if current.key == key:
                    current.value = value
                    return  # Key found and updated, exit the function
                current = current.next

            # Key not found, append the new node to the linked list
            a.next = self.hashtable[z]
            self.hashtable[z] = a
    def get(self,key):
        z = key%7
        c = self.hashtable[z]
        print(c.key)
        if c.key == key:
            return c.value
        else:
            while c:
                if c.key ==key:
                    return c.value
                c=c.next
        return -1      

a =dictionary()
a.put(3,4)
a.put(10,5)
print(a.get(3),a.get(10))
# print(a.get(6))

   

