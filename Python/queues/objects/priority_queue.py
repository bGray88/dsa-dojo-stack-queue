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
        tmp = []
        for idx, queue in enumerate(self.data):
            while not queue.empty() and idx:
                tmp.append(queue.dequeue())
        for plane in tmp:
            diff_time   = self.time - int(plane.expected_departure)
            recov_time  = (int(plane.expected_landing) - int(plane.expected_departure)) * 0.8
            adjstd_time = self.time + recov_time
            
            if diff_time > 0 and diff_time <= 15:
                self.enqueue(1, plane)
            elif adjstd_time > int(plane.expected_departure) and adjstd_time <= int(plane.expected_landing):
                self.enqueue(2, plane)
            elif int(plane.expected_departure) > self.time:
                self.enqueue(3, plane)
            else:
                self.enqueue(4, plane)
        

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
