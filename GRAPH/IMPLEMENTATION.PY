class graph:
    def __init__(self,dictt=None):
        if dictt is None:
            dictt = {}
        self.dictt = dictt
    def addvertex(self,vertex):
        if vertex not in self.dictt:
            self.dictt[vertex] = []  # Create an empty list for the new vertex
        else:
            return False
    def addedge(self,ver1,ver2):
        if ver1 in self.dictt.keys() and ver2 in self.dictt.keys():
            self.dictt[ver1].append(ver2)
            self.dictt[ver2].append(ver1)
        else:return False
    def removeedge(self,ver1,ver2):
        if ver1 in self.dictt.keys() and ver2 in self.dictt.keys():
            self.dictt[ver1].remove(ver2)
            self.dictt[ver2].remove(ver1)
        else:return False
    def remove_vertex(self,vertex):
        if vertex in self.dictt.keys():
            for othervertex in self.dictt[vertex]:
                self.dictt[othervertex].remove(vertex)
            del self.dictt[vertex]
            return True
        return False

    def show(self):
        for vertex in self.dictt:

            print(vertex,"-->",self.dictt[vertex])

grph = graph(None)
grph.addvertex("p")
grph.addvertex("rai")
grph.addedge("p","rai")

grph.show()
grph.removeedge("p","rai")
grph.show()
grph.remove_vertex("p")

grph.show()
