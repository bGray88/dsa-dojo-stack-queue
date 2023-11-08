from .linked_list import LinkedList

class Queue:
    def __init__(self):
        self.data = LinkedList()

    def count(self):
        return self.data.count()

    def peek(self):
        return self.data.find_value_at(0)
    
    def last(self):
        return self.data.last().data
    
    def empty(self):
        return self.data.count() == 0

    def enqueue(self, element):
        self.data.append(element)

    def dequeue(self):
        first = self.peek()
        self.data.delete_at_position(self.data.find_index_of(first))
        return first
    