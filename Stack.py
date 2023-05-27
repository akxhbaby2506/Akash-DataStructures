class ArrayStack:
    def __init__(self):
        self.data = []
        
    def push(self, value):
        self.data.append(value)
        print(value," is pushed successfully! ")
        
    def pop(self):
        if len(self.data) == 0:
            print("Stack is Empty...!")
            print("Please undergo push operation!")
        else:
            self.data.pop()
            print("POP the element from the stack")
        
    def top(self):
        if len(self.data) == 0:
            print("Stack is Empty...!")
            print("Please undergo push operation!")
        else:
            print(self.data[-1])
            
    def display(self):
        print(self.data)
        
stack = ArrayStack()
stack.display()
stack.top()
stack.pop()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)
stack.display()
stack.top()
stack.pop()
stack.pop()
stack.top()
stack.display()
