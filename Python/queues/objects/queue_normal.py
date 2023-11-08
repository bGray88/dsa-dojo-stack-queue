import copy

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

    def find_place(self, name):
        tmp_queue = copy.deepcopy(self.data)
        count = 0
        while tmp_queue and tmp_queue[0].name != name:
            del tmp_queue[0]
            count += 1
        return count, tmp_queue and tmp_queue[0].name == name
