class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self  #self will become parent of the child
        self.children.append(child)

    def print_tree(self):
        spaces = " " * self.get_level() * 3  #increaces the initial spacing 3 tyms
        prefix = spaces + "|__" if self.parent else ""
        print(prefix+self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level = level + 1
            p = p.parent   ##Not Understood line
        return level

def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Lunix"))
    laptop.add_child(TreeNode("Windows"))
    laptop.add_child(TreeNode("Mac"))

    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("Google"))
    cellphone.add_child(TreeNode("Readmi"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("LG"))
    tv.add_child(TreeNode("SONY"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    # print(tv.get_level()) --> #tv is in level-1
    return root

if __name__ == '__main__':
    root = build_product_tree()
    #print(root)   --> <__main__.TreeNode object at 0x000001EF62F63FD0>
    #print(root.get_level()) --> 0
    root.print_tree()
    pass
