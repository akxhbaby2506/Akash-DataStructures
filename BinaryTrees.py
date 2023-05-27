class Tree:
    
    def __init__(self, value = None):
        self.value = value
        
        if self.value:
            self.left = Tree()
            self.right = Tree()
        else:
            self.left = None
            self.right = None
            
    def isEmpty(self):
        return self.value == None
    
    def find(self,v):
        
        if v == self.value:
            return True
        
        if v < self.value:
            return self.left.find(v)
        
        if v > self.value:
            return self.right.find(v)
        
    def insert(self,v):
        
        if self.isEmpty():
            self.value = v
            self.left = Tree()
            self.right = Tree()
            
        if self.value > v:
            self.left.insert(v)
            return
        
        if self.value < v:
            self.right.insert(v)
            return
    
    # For different types of Traversal
    def preorder(self):
        return ([self.value]+self.left.preorder()+self.right.preorder())
    
    def inorder(self):
        return (self.left.inorder()+[self.value]+self.right.inorder())
    
    def postorder(self):
        return (self.left.postorder()+self.right.postorder()+[self.value])
    
    def print_tree(self):
        print(self.value)

t = Tree(15)
t.insert(19)
t.insert(13)
t.insert(14)
t.insert(10)
t.insert(17)
t.insert(23)
t.print_tree()