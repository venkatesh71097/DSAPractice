from collections import deque
from heapq import heappop, heappush

class IterableMixin:
    def __len__(self):
        return len(self._elements)
    def __iter__(self):
        while len(self) > 0:
            yield self.dequeue()

class Queue(IterableMixin):
    def __init__(self, *elements):
        self._elements = deque(elements)

    def enqueue(self, element):
        return self._elements.append(element)

    def dequeue(self):
        return self._elements.popleft()
    
class Stack(Queue):
    def dequeue(self):
        return self._elements.pop()

class PriorityQueue(IterableMixin):
    def __init__(self):
        self._elements = []
    
    def enqueue_with_priority(self, priority, element):
        heappush(self._elements, (priority, element))
    
    def dequeue(self):
        return heappop(self._elements)[1]