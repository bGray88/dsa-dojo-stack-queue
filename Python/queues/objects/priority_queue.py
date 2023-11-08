from .queue_normal import Queue

class PriorityQueue(Queue):
    def __init__(self):
        super().__init__()
        self.planes = 0
        self.time   = 0
        for _ in range(6):
            self.data.append(Queue())

    def total_count(self):
        return self.planes
    
    def current_time(self):
        return self.time
    
    def tick(self, i):
        self.time += i

    def audit(self):
        pass

    def queue_wait(self, obj_name):
        count = 0
        found = False
        for queue in self.data:
            current, found = queue.find_place(obj_name)
            count += current
            if found: break
        return count if found else None

    def enqueue(self, pos, obj):
        self.planes += 1
        self.data[pos].enqueue(obj)

    def next(self):
        self.planes -= 1
        for idx, queue in enumerate(self.data):
            if not queue.empty():
                return self.data[idx].dequeue()

    def peek(self):
        for idx, queue in enumerate(self.data):
            if not queue.empty():
                return self.data[idx].peek()

    def status(self):
        return self.__str__()

    def __str__(self):
        return "{\n" + \
            "\t0 => " + str(self.data[0].count()) + ",\n" \
            "\t1 => " + str(self.data[1].count()) + ",\n" \
            "\t2 => " + str(self.data[2].count()) + ",\n" \
            "\t3 => " + str(self.data[3].count()) + ",\n" \
            "\t4 => " + str(self.data[4].count()) + ",\n" \
            "\t5 => " + str(self.data[5].count()) + ",\n" \
        "}"
