import heapq

class PriorityQueue(object):
    def __init__(self):
        self.heap = []
        self.exists = set()

    def __bool__(self):
        return len(self.heap) != 0

    def __contains__(self, item):
        return item in self.exists

    def push(self, item, priority):
        if item in self.exists:
            self.heap.remove(item)
            heapq.heapify(self.heap)
        self.exists.add(item)
        heapq.heappush(self.heap, (item, priority))

    def pop(self):
        item, priority = heapq.heappop(self.heap)
        self.exists.remove(item)
        return item, priority
