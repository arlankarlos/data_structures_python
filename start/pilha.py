# Pilha em Python - Stack
from random import randint
class Stack:
    def __init__(self):
        self.__dados = []
        self.len_stack = 0

    def push(self, valor):
        self.__dados.append(valor)
        self.len_stack += 1

    def pop(self):
        if not self.empty():
            self.len_stack -= 1
            return self.__dados.pop(self.len_stack)
    
    def top(self):
        if not self.empty():
            return self.__dados[-1]
        return None
    
    def empty(self):
        if self.len_stack == 0:
            return True
        else:
            return False
        
    def length(self):
        return self.len_stack

nova_stack = Stack()

for i in range(10):
    nova_stack.push(i+1)
    
print(nova_stack)
print('Esta vazia?', nova_stack.empty())

for i in range(10):
    nova_stack.pop()


print('Esta vazia?', nova_stack.empty())