from .linked_list import LinkedList

class Stack:
    def __init__(self):
        self.data = LinkedList()

    def count(self):
        return self.data.count()
    
    def empty(self):
        return self.count() == 0

    def peek(self):
        return self.data.last().data if not self.empty() else None

    def push(self, element):
        self.data.append(element)

    def pop(self):
        last = self.data.last().data
        self.data.delete_at_position(self.data.find_index_of(last))
        return last

    def reverse_stack(self):
        self.data.reverse_list()

    def print_stack(self):
        return self.data.print_list()
