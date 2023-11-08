class Queue:
    def __init__(self):
        self.data = []

    def count(self):
        return len(self.data)

    def peek(self):
        return self.data[0]
    
    def last(self):
        return self.data[-1]
    
    def empty(self):
        return self.count() == 0

    def enqueue(self, element):
        self.data.append(element)

    def dequeue(self):
        first = self.data[0]
        del self.data[0]
        return first
    