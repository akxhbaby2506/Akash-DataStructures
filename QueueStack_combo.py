class Data_Structure:
    
    def __init__(self):
        self.data = []

    def isempty(self):
        return len(self.data)==0

    def insert(self,ele):
        self.data.append(ele)

    def dequeue(self):
        if self.isempty():
            print("Array is Empty")
        else:
            print("It's gonna undergo queue operation")
            print("The element which is gonna be poped is ",self.data.pop(0))

    def pop(self):
        if self.isempty():
            print("Array is Empty")
        else:
            print("It's gonna undergo queue operation")
            print("The element which is gonna be poped is ", self.data.pop())

    def top(self):
        if self.isempty():
            print("Array is Empty")
        else:
            print("If it is Queue, the topmost element is: ",self.data[0])
            print("If it is Stack, the topmost element is: ",self.data[-1])

    def display(self):
        print(self.data)

d = Data_Structure()
d.display()
d.pop()
d.dequeue()
d.top()
print()
d.insert(100)
d.insert(200)
d.insert(300)
d.insert(400)
d.insert(500)
d.insert(600)
d.insert(700)
d.insert(800)

d.display()
d.top()
d.dequeue()
d.pop()
d.display()
d.top()