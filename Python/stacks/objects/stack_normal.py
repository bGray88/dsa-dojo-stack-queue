class Stack:
    VALID_OPEN  = { '{': '}', '[': ']', '(': ')' }
    VALID_CLOSE = { '}': '{', ']': '[', ')': '(' }

    def __init__(self):
        self.data = []

    def count(self):
        return len(self.data)
    
    def empty(self):
        return self.count() == 0

    def peek(self):
        return self.data[-1] if not self.empty() else None

    def push(self, element):
        self.data.append(element)

    def pop(self):
        last = self.data[-1]
        del self.data[-1]
        return last

    def reverse_stack(self):
        tmp_stack = self.data
        self.data = []
        while tmp_stack:
            self.push(tmp_stack.pop())

    def print_stack(self):
        return ''.join(self.data)
    
    def validate(self):
        tmp_stack = self.data
        tmp_stack.reverse()
        collect   = []
        while tmp_stack:
            last = tmp_stack.pop()
            if Stack.VALID_OPEN.get(last):
                collect.append(last)
            else:
                if not collect or Stack.VALID_CLOSE.get(last) != collect.pop():
                    return False
        return True
