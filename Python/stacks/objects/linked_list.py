from .node import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def last(self):
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            return current

    def count(self):
        count   = 0
        current = self.head
        if current:
            count += 1
            while current.next:
                count  += 1
                current = current.next
        return count

    def find_index_of(self, data):
        count   = 0
        current = self.head
        if current:
            while count < self.count() and current and data != current.data:
                count  += 1
                current = current.next
        return count if current else None
      
    def find_value_at(self, pos):
        count   = 0
        current = self.head
        if current and (pos <= self.count()):
            while count < pos:
                count  += 1
                current = current.next
        return current.data if current else None
    
    def append(self, data):
        if self.head:
            current      = self.last()
            current.next = Node(data)
        else:
            self.head    = Node(data)

    def insert_at_position(self, pos, data):
        if pos == 0:
            self.swap("head", Node(data))
        elif self.head and (pos < self.count()):
            count   = 0
            current = self.head
            while count < (pos - 1):
                count  += 1
                current = current.next
            self.swap(current, Node(data))
        elif pos >= self.count():
            self.append(data)

    def delete_at_position(self, pos):
        if self.head and (pos < self.count()):
            count   = 0
            current = self.head
            while count < (pos - 1):
                count  += 1
                current = current.next
            self.swap(current, pos)

    def delete_value(self, data):
        if self.head:
            count = 0
            current = self.head
            while count < self.count() and current and data != current.data:
                  count  += 1
                  current = current.next
            self.delete_at_position(count)

    def reverse_list(self):
        count = 0
        while count < self.count():
            self.insert_at_position(count, self.last().data)
            self.delete_at_position(self.count() - 1)
            count += 1

    def swap(self, current, value):
        if type(current) == str:
            next           = self.head
            self.head      = value
            self.head.next = next
        elif type(value) == int:
            if value == 0:
                self.head    = current.next
            elif current.next.next:
                current.next = current.next.next
            else:
                current.next = None
        else:
            next         = current.next
            current.next = value
            current      = current.next
            current.next = next

    def print_list(self):
        printed = ""
        current = self.head
        if current:
            printed += current.data
            while current.next:
                current = current.next
                printed += current.data
        return printed
    