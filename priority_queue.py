import heapq

class PriorityQueue(object):
    REMOVED = 'REMOVED'

    def __init__(self):
        self.heap = []
        self.exists = dict()

    def __bool__(self):
        return len(self.heap) != 0

    def __contains__(self, item):
        return item in self.exists

    def push(self, item, priority):
        if item in self.exists:
            entry = self.exists.pop(item)
            entry[0] = self.REMOVED
        entry = [item, priority]
        self.exists[item] = entry
        heapq.heappush(self.heap, entry)

    def pop(self):
        while self.heap:
            item, priority = heapq.heappop(self.heap)
            if item is not self.REMOVED:
                del self.exists[item]
                return item, priority
