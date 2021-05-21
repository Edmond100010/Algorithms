class Tree():
    def __init__(self,root):
        self.l = None
        self.r = None
        self.root = root

    def getLChild(self):
        return self.l
    def getRChild(self):
        return self.r
    def setNodeValue(self,value):
        self.root = value
    def getNodeValue(self):
        return self.root

    def insertR(self,node):
        if self.r == None:
            self.r = Tree(node)
        else:
            tree = Tree(node)
            tree.r = self.r
            self.r = tree

    def insertL(self,node):
        if self.l == None:
            self.l = Tree(node)
        else:
            tree = Tree(node)
            tree.l = self.l
            self.l = tree

    def printTree(self, node):
        if(node!=None):
            self.printTree(node.l)
            print(node.root)
            self.printTree(node.r)





