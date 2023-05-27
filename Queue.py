class ArrayQueue:
    def __init__(self):
        self.data = []
        
    # REAR :- Elements are inserted    
    def enqueue(self, item):
        self.data.append(item)
        print(item, " is been inserted")
    
    # FRONT :- Elements are deleted
    def dequeue(self):
        if len(self.data) == 0:
            print("Array is Empty...!")
            
        else:
            self.data.pop(0)
    
    # This is to mention the top most element that can be removed from the array
    def top(self):
        if len(self.data) == 0:
            print("Array is Empty...!")
        else:
            print(self.data[0])
            
    def display(self):
        print(self.data)

queue = ArrayQueue()
queue.display()
queue.top()
queue.dequeue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)
queue.display()
queue.top()
queue.dequeue()
queue.dequeue()
queue.top()
queue.display()
