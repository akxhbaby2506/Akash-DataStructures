"""
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None


    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data)+' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next

        return count

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count+=1

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.insert_at(1,"blueberry")
    ll.remove_at(2)
    ll.print()

    ll.insert_values([45,7,12,567,99])
    ll.insert_at_end(67)
    ll.print()
"""
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBeg(self,data):
        node = Node(data, self.head)
        self.head = node

    def insertAtEnd(self, data):
        if self.head is None:
            self.head = Node(data,None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def printlist(self):
        if self.head is None:
            print("Linked List is Empty")
            return

        itr = self.head
        llstr = ''

        while itr:
            llstr = llstr + str(itr.data) + '-->'
            itr = itr.next

        print(llstr)

    def listvalued(self, data_list):
        self.head = None
        for data in data_list:
            self.insertAtEnd(data)

    def removeAt(self, index):
        if index<0 or index>=self.getLength():
            raise Exception("Invalid Index")
        if index==0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count = count+1

    def insertAt(self, index,data):
        if index<0 or index>self.getLength():
            raise Exception("Invalid index")
        if index==0:
            self.insertAtBeg(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count = count + 1
            
    def insertAfterValue(self, dataAfter, dataInsert):
        itr = self.head

        if itr is None:
            return

        if itr.data == dataAfter:
            itr.next = Node(dataInsert, itr.next)
            return

        while itr:
            if itr.data==dataAfter:
                itr.next = Node(dataInsert, itr.next)
                break
            itr = itr.next

    def deleteByValue(self, data):
        itr = self.head

        if itr is None:
            return

        if itr.data == data:
            self.head = itr.next
            return

        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next

    def getLength(self):
        count = 0
        itr = self.head
        while itr:
            count = count+1
            itr = itr.next
        return count

if __name__ == '__main__':
    ll = LinkedList()
    ll.printlist()
    print()
    ll.insertAtBeg(5)
    ll.insertAtBeg(8)
    ll.insertAtEnd(13)
    ll.insertAtEnd(97)
    ll.insertAtBeg(36)
    print(ll.getLength())
    ll.removeAt(4)
    ll.insertAt(3,32)
    ll.printlist()
    print()
    ll.listvalued(["Ram","Krishna","Buddha","Kalki"])
    print(ll.getLength())
    ll.removeAt(2)
    ll.insertAt(0, "ParashuRam")
    ll.insertAt(3, "Hanuman")
    ll.printlist()
    print()
    print("insertByValue() and deleteByValue")
    ll.listvalued(['mango','apple','bannana','papaya'])
    ll.printlist()
    ll.insertAfterValue('apple','perry')
    ll.insertAfterValue('bannana','jackfruit')
    ll.deleteByValue('apple')
    ll.deleteByValue('mango')
    ll.printlist()