import heapq


class Person:
    def __init__(self, name):
        self.name = name
        
    def __repr__(self):
        return self.name
    

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._indice = 0
    
    
    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._indice, item))
        self._indice +=1
        
        
    def remover(self):
        return heapq.heappop(self._queue)[-1]


new_queue = PriorityQueue()
new_queue.push('Joaquim', 20)
new_queue.push('Maria', 22)
new_queue.push('Jose', 18)
new_queue.push('Joao', 25)

for item in range(new_queue._indice):
    print(new_queue.remover())
