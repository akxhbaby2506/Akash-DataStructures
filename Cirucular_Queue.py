class CircularQueue:
    
    def __init__(self, DEFAULT_CAPACITY = 5):
        self.DEFAULT_CAPACITY = DEFAULT_CAPACITY
        self.data = [None]*DEFAULT_CAPACITY
        self.front = 0
        self.rear = 0
        self.size = 0

    def isFull(self):
        return self.size == self.DEFAULT_CAPACITY

    def isEmpty(self):
        return self.size == 0

    def enqueue(self,ele):
        if self.isFull():
            print("Array is Full")
        else:
            self.data[self.rear] = ele
            self.size = self.size+1
            self.rear = self.rear+1

    def dequeue(self):
        if self.isEmpty():
            print("Array is Empty")
        else:
            self.data[self.front] = None
            self.front = self.front+1
            self.size = self.size-1
            

    def display(self):
        print(self.data)
        
    def first(self):
        if self.isEmpty():
            print("Array is Empty")
        else:
            print(self.data[0])

cqueue = CircularQueue()
cqueue.display()
cqueue.enqueue(10)
cqueue.enqueue(20)
cqueue.first()
cqueue.enqueue(30)
cqueue.enqueue(40)
cqueue.enqueue(50)
cqueue.display()
cqueue.first()
cqueue.enqueue(60)
cqueue.enqueue(70)
cqueue.display()
cqueue.dequeue()
cqueue.dequeue()
cqueue.first()
cqueue.display()
