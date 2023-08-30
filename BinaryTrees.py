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
            return self.left.insert(v)
        
        if self.value < v:
            return self.right.insert(v)
    
    # For different types of Traversal
    def preorder(self):
        if self.isEmpty():
            return []
        return ([self.value]+self.left.preorder()+self.right.preorder())        
    
    def inorder(self):
        if self.isEmpty():
            return []
        return (self.left.inorder()+[self.value]+self.right.inorder())
    
    def postorder(self):
        if self.isEmpty():
            return []
        return (self.left.postorder()+self.right.postorder()+[self.value])
    
    #Print the Tree
    def print_tree(self,level=0, prefix="Root: "):
        indent = "   "*level
        print(indent+prefix+str(self.value))
        
        if self.left:
            self.left.print_tree(level+1,prefix="L--")
        if self.right:
            self.right.print_tree(level+1,prefix="R--")
    
    #Print the tree with respect to their possitions
    
    def print_inorder(self):
        result = self.inorder()
        print("Inorder Traversal:")
        for value in result:
            print(value, end=" ")
        print("\n")

    def print_preorder(self):
        result = self.preorder()
        print("Preorder Traversal:")
        for value in result:
            print(value, end=" ")
        print("\n")

    def print_postorder(self):
        result = self.postorder()
        print("Postorder Traversal:")
        for value in result:
            print(value, end=" ")
        print("\n")
        
t = Tree(15)
t.insert(19)
t.insert(13)
t.insert(14)
t.insert(10)
t.insert(17)
t.insert(20)
t.insert(23)

t.print_tree()
t.print_preorder()
t.print_inorder()
t.print_postorder()
