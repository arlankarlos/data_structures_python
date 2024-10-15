# Fila em Python - Queue
from random import randint


class Queue:
    def __init__(self):
        self.queue = []
        self.len_queue = 0
        
    def push(self, valor):
        self.queue.append(valor)
        self.len_queue += 1
        
    def pop(self):
        if not self.empty(): 
            self.len_queue -= 1
            return self.queue.pop(0)
        
    def empty(self):
        if self.len_queue == 0:
            return True
        else:
            return False
        
    def length(self):
        return self.len_queue
    
    def front(self):
        if not self.empty():
            return self.queue[0]
        return None
    
nova_fila = Queue()

for i in range(10):
    nova_fila.push(i+1)
    
print('Esta vazia?', nova_fila.empty())
print(nova_fila.length())    
for i in range(10):
    print(f"{nova_fila.pop()} - {nova_fila.length()+1}")
    
print('Esta vazia?', nova_fila.empty())
print(nova_fila.length())    