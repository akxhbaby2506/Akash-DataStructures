class Empty(Exception):
    pass

class LinkedStack:
    
    class _Node:
        def __init__(self,element,next):
            self.element = element
            self.next = next
            
    def __init__(self):
        self.head = None
        self.size = 0
        
    def __len__(self):
        return len(self.size)
    
    def is_empty(self):
        return self.size == 0
    
    def push(self,e):
        self.head = self._Node(e,self.head)
        self.size = self.size + 1
        
    def pop(self):
        if self.is_empty():
            raise Empty("Stack is Empty")
        answer = self.head.element
        self.head = self.head.next
        self.size = self.size - 1
        return answer
    
    def top(self):
        if self.is_empty():
            raise Empty("Stack is Empty")
        return self.head.element
    
    def display(self):
        pri = self.head
        while pri is not None:
            print(pri.element)
            pri = pri.next

ll = LinkedStack()
ll.push(50)
ll.push(40)
ll.push(30)
ll.push(20)
ll.push(10)
ll.display()
print()
ll.top()
print()
ll.pop()
ll.pop()
print()
ll.display()
print()
ll.top()
print()
ll.display()